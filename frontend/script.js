(function () {
  const root = document.documentElement;
  const THEME_KEY = "mlp_demo_theme";

  function applyTheme(theme) {
    root.setAttribute("data-theme", theme);
    const icon = document.querySelector("#themeToggle i");
    if (icon) {
      icon.className = theme === "dark" ? "bi bi-sun" : "bi bi-moon-stars";
    }
  }

  const storedTheme = localStorage.getItem(THEME_KEY) || "light";
  applyTheme(storedTheme);

  const themeToggle = document.getElementById("themeToggle");
  if (themeToggle) {
    themeToggle.addEventListener("click", function () {
      const next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      localStorage.setItem(THEME_KEY, next);
      applyTheme(next);
      updateChartsForTheme(next);
    });
  }

  const navLinks = document.querySelectorAll(".sidebar .nav-link");
  const panels = document.querySelectorAll(".section-panel");

  navLinks.forEach(function (link) {
    link.addEventListener("click", function (event) {
      event.preventDefault();
      const target = link.getAttribute("data-section");

      navLinks.forEach((n) => n.classList.remove("active"));
      panels.forEach((p) => p.classList.remove("active"));

      link.classList.add("active");
      const panel = document.getElementById("section-" + target);
      if (panel) {
        panel.classList.add("active");
      }

      const sidebar = document.getElementById("sidebar");
      if (sidebar && window.innerWidth < 992) {
        sidebar.classList.remove("open");
      }
    });
  });

  const openSidebar = document.getElementById("openSidebar");
  const closeSidebar = document.getElementById("closeSidebar");
  const sidebar = document.getElementById("sidebar");

  if (openSidebar && sidebar) {
    openSidebar.addEventListener("click", function () {
      sidebar.classList.add("open");
    });
  }

  if (closeSidebar && sidebar) {
    closeSidebar.addEventListener("click", function () {
      sidebar.classList.remove("open");
    });
  }

  const chartRegistry = [];

  function buildCharts() {
    if (typeof Chart === "undefined") return;

    const commonOpts = {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { labels: { color: getColor("text") } }
      },
      scales: {
        x: {
          ticks: { color: getColor("textSoft") },
          grid: { color: getColor("grid") }
        },
        y: {
          ticks: { color: getColor("textSoft") },
          grid: { color: getColor("grid") }
        }
      }
    };

    createChart("throughputChart", {
      type: "line",
      data: {
        labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        datasets: [{
          label: "Records / hour",
          data: [1800, 2200, 2400, 2300, 2600, 2100, 1950],
          borderColor: "#0f9d9a",
          backgroundColor: "rgba(15,157,154,0.2)",
          tension: 0.35,
          fill: true
        }]
      },
      options: commonOpts
    });

    createChart("performanceChart", {
      type: "bar",
      data: {
        labels: ["MAE", "RMSE", "R2"],
        datasets: [{
          label: "Latest Model",
          data: [244, 362, 0.91],
          backgroundColor: ["#f59e0b", "#0b7f95", "#16a34a"]
        }]
      },
      options: {
        ...commonOpts,
        scales: {
          x: commonOpts.scales.x,
          y: {
            ...commonOpts.scales.y,
            beginAtZero: true
          }
        }
      }
    });

    createChart("priceTrendChart", {
      type: "line",
      data: {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        datasets: [{
          label: "Avg Price",
          data: [4900, 5100, 5350, 5600, 6100, 5900],
          borderColor: "#0b7f95",
          backgroundColor: "rgba(11,127,149,0.2)",
          fill: true,
          tension: 0.3
        }]
      },
      options: commonOpts
    });

    createChart("routeChart", {
      type: "doughnut",
      data: {
        labels: ["DEL-BOM", "BLR-DEL", "MAA-KOL", "HYD-BOM"],
        datasets: [{
          data: [34, 27, 21, 18],
          backgroundColor: ["#0f9d9a", "#0b7f95", "#f59e0b", "#7c3aed"]
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { labels: { color: getColor("text") } }
        }
      }
    });
  }

  function createChart(id, config) {
    const canvas = document.getElementById(id);
    if (!canvas) return;
    const chart = new Chart(canvas, config);
    chartRegistry.push(chart);
  }

  function getColor(token) {
    const styles = getComputedStyle(document.documentElement);
    if (token === "text") return styles.getPropertyValue("--text").trim();
    if (token === "textSoft") return styles.getPropertyValue("--text-soft").trim();
    return "rgba(122,140,169,0.25)";
  }

  function updateChartsForTheme() {
    chartRegistry.forEach(function (chart) {
      if (chart.options.scales) {
        chart.options.scales.x.ticks.color = getColor("textSoft");
        chart.options.scales.y.ticks.color = getColor("textSoft");
        chart.options.scales.x.grid.color = getColor("grid");
        chart.options.scales.y.grid.color = getColor("grid");
      }
      if (chart.options.plugins && chart.options.plugins.legend && chart.options.plugins.legend.labels) {
        chart.options.plugins.legend.labels.color = getColor("text");
      }
      chart.update();
    });
  }

  buildCharts();
})();
