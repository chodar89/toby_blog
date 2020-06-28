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