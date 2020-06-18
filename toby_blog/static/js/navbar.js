const navColor = () => {
  const navBg = document.querySelector('.nav-bg'),
  navLine = document.querySelector('.nav-line'),
  navLinks = document.querySelectorAll('.nav-links li a');

  window.onscroll = () => {
    let top = window.scrollY;
    if (top >= 30) {
      navBg.classList.add('nav-active');
      navLine.style.opacity = 1;
      navLinks.forEach(link => {
        link.classList.add('nav-links-active');
      });
    } else {
      navBg.classList.remove('nav-active');
      navLine.style.opacity = 0;
      navLinks.forEach(link => {
        link.classList.remove('nav-links-active');
      });
    }
  }
}

navColor();