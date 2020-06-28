const clapShow = () => {
  const clap = document.querySelector(".clap-container");
  console.log(clap);
  window.onscroll = () => {
    let top = window.scrollY;
    console.log("blabla");
    let windowHeight = window.innerHeight;
    let clapShowHeight = (windowHeight * 0.45);
    if (top >= clapShowHeight) {
      clap.style.opacity = 1;
    } else {
      clap.style.opacity = 0;
    }
  }
}

clapShow();