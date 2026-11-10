// Loads a page in WebKit (the engine behind Safari and every iPhone browser) at phone width,
// prints any elements that stick out past the right edge and saves a PNG of the plug-in grid.
// usage: swiftc -O tools/webkitshot.swift -o /tmp/webkitshot && /tmp/webkitshot <url> <out.png> [width]
import AppKit
import WebKit

let args = CommandLine.arguments
let url = URL (string: args[1])!
let out = args[2]
let width = CGFloat (Double (args.count > 3 ? args[3] : "390")!)

class Loader: NSObject, WKNavigationDelegate {
    let web: WKWebView
    init (_ w: WKWebView) { web = w }
    func webView (_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        DispatchQueue.main.asyncAfter (deadline: .now() + 2.0) {
            let js = """
            (() => { const w = innerWidth, c = document.querySelector('.pcard'), i = c && c.querySelector('img');
              const wide = [...document.querySelectorAll('body *')].filter(e => e.getBoundingClientRect().right > w + 1).length;
              return JSON.stringify({ innerWidth: w, scrollWidth: document.documentElement.scrollWidth,
                card: c && Math.round(c.getBoundingClientRect().width), img: i && Math.round(i.getBoundingClientRect().width), ratio: i && (i.parentElement.getBoundingClientRect().width / i.parentElement.getBoundingClientRect().height).toFixed(3),
                elementsPastEdge: wide, which: [...document.querySelectorAll("body *")].filter(e => e.getBoundingClientRect().right > w + 1).map(e => e.tagName + "." + (e.getAttribute("class")||"") + ":" + Math.round(e.getBoundingClientRect().right)).slice(0,8), css: [...document.styleSheets].map(s => s.href || '').join(' ') }); })()
            """
            self.web.evaluateJavaScript (js) { r, e in
                print (r ?? e ?? "no result")
                let cfg = WKSnapshotConfiguration()
                cfg.rect = CGRect (x: 0, y: 0, width: width, height: 1600)
                self.web.evaluateJavaScript ("window.scrollTo(0, document.getElementById('plugins') ? document.getElementById('plugins').offsetTop - 80 : 0)") { _, _ in
                    DispatchQueue.main.asyncAfter (deadline: .now() + 0.5) {
                        let cfg2 = WKSnapshotConfiguration()
                        self.web.takeSnapshot (with: cfg2) { img, err in
                            if let img = img, let tiff = img.tiffRepresentation, let rep = NSBitmapImageRep (data: tiff),
                               let png = rep.representation (using: .png, properties: [:]) {
                                try? png.write (to: URL (fileURLWithPath: out)); print ("saved", out)
                            } else { print ("snapshot failed", err as Any) }
                            exit (0)
                        }
                    }
                }
            }
        }
    }
}

let app = NSApplication.shared
let cfg = WKWebViewConfiguration()
let web = WKWebView (frame: CGRect (x: 0, y: 0, width: width, height: 844), configuration: cfg)
web.customUserAgent = "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1"
let window = NSWindow (contentRect: web.frame, styleMask: [.borderless], backing: .buffered, defer: false)
window.contentView = web
let loader = Loader (web)
web.navigationDelegate = loader
web.load (URLRequest (url: url, cachePolicy: .reloadIgnoringLocalCacheData))
DispatchQueue.main.asyncAfter (deadline: .now() + 30) { print ("timeout"); exit (1) }
app.run()
