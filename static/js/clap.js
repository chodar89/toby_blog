$(".clap-btn").click(function(e){
  e.preventDefault()
  var this_ = $(this)
  var clapUrl = this_.attr("data-href")
  $.ajax({
    url: clapUrl,
    method: "GET",
    data:{},
    success: function(data) {
      let clapCount = document.querySelector(".clap-count")
      clapCount.innerHTML = data.claps;
    }, error: function(error){
      console.log(error)
      console.log("error")
    }
  })
})

// Clap show hide

const clapShow = () => {
  const clap = document.querySelector(".clap-container");
  window.onscroll = () => {
    let top = window.scrollY;
    let windowHeight = window.innerHeight;
    let clapShowHeight = (windowHeight * 0.6) + 60
    if (top >= clapShowHeight) {
      clap.style.opacity = 1;
    } else {
      clap.style.opacity = 0;
    }
  }
}

clapShow();