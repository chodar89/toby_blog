const navColor = () => {
  const navBg = document.querySelector('.nav-bg'),
  navLine = document.querySelector('.nav-line'),
  navLinks = document.querySelector('.nav-links');

  window.onscroll = () => {
    let top = window.scrollY;
    if (top >= 30) {
      navBg.classList.add('nav-bg-white');
      navLine.style.opacity = 1;
      navLinks.classList.add('nav-links-dark');
    } else {
      navBg.classList.remove('nav-bg-white');
      navLine.style.opacity = 0;
      navLinks.classList.remove('nav-links-dark');
    }
  }
}

navColor();