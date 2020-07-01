// Navigation slide bar
const navSlide = () => {
  const burger = document.querySelector(".burger");
  const nav = document.querySelector(".nav-links");
  const navLinks = document.querySelectorAll(".nav-links li");
  const navSocial = document.querySelector(".nav-social");

  burger.addEventListener("click", () => {
    // Toggle Nav
    nav.classList.toggle("nav-active");

    // Animate Links
    navLinks.forEach((link, index) => {
      countIndex = navLinks.length;
      if (link.style.animation) {
        link.style.animation = '';
        nav.style.transition = '';
        navSocial.style.animation = '';
      } else {
        nav.style.transition = 'transform 0.5s ease-in';
        link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.3}s`;
        navSocial.style.animation = `navSocialFade 1.3s ease forwards ${countIndex / 7 +0.3}s`;
      }
    })
  });
};

navSlide();