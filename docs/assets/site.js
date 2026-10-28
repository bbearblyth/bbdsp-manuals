// Filter the plugin grid, track the section in view, and pause motion when asked.
(function () {
  var seg = document.querySelector (".seg");
  if (seg) seg.addEventListener ("click", function (e) {
    var b = e.target.closest ("button"); if (!b) return;
    seg.querySelectorAll ("button").forEach (function (x) { x.classList.toggle ("on", x === b); });
    var k = b.dataset.filter;
    document.querySelectorAll (".pcard").forEach (function (c) { c.hidden = k !== "all" && c.dataset.kind !== k; });
  });

  var links = document.querySelectorAll (".toc a");
  if (links.length && "IntersectionObserver" in window) {
    var byId = {}; links.forEach (function (a) { byId[a.getAttribute ("href").slice (1)] = a; });
    var io = new IntersectionObserver (function (entries) {
      entries.forEach (function (en) {
        if (!en.isIntersecting) return;
        links.forEach (function (a) { a.classList.remove ("on"); });
        var a = byId[en.target.id]; if (a) a.classList.add ("on");
      });
    }, { rootMargin: "-80px 0px -70% 0px" });
    Object.keys (byId).forEach (function (id) { var s = document.getElementById (id); if (s) io.observe (s); });
  }

  if (window.matchMedia && matchMedia ("(prefers-reduced-motion: reduce)").matches)
    document.querySelectorAll ("svg.motion").forEach (function (s) { if (s.pauseAnimations) s.pauseAnimations(); });
})();
