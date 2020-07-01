const clapShow = () => {
  const clap = document.querySelector(".clap-container");
  window.addEventListener('scroll', function(e) {
    let top = window.scrollY;
    let windowHeight = window.innerHeight;
    let documentHeight = document.body.scrollHeight;
    let clapShowHeight = (windowHeight * 0.4);
    let clapHideHeight;
    if (windowHeight < 500) {
      clapHideHeight = documentHeight - 450;
    } else {
      clapHideHeight = documentHeight - 100;
    }
    if (top >= clapShowHeight && top < clapHideHeight) {
      clap.style.opacity = 1;
    } else {
      clap.style.opacity = 0;
    }
  })
}

const clapJolly = () => {
  const clap = document.querySelector(".clap-btn");
  const count = document.querySelector(".clap-count")
  clap.classList.remove("clap-jello");
  count.classList.remove("count-add-one");
  void clap.offsetWidth;
  void count.offsetWidth;
  clap.classList.add("clap-jello");
  count.classList.add("count-add-one");
}

clapShow();