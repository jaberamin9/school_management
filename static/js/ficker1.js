const wrapper = document.querySelector(".wrapper_piker"),
fileName = wrapper.querySelector(".file-name"),
button = wrapper.querySelector("#button"),
btn = wrapper.querySelector("#btn"),
cancelBtn = wrapper.querySelector("#cancel-btn i"),
img = wrapper.querySelector("img");
let regExp = /[0-9a-zA-Z\^\&\'\@\{\}\[\]\,\$\=\!\-\#\(\)\.\%\+\~\_ ]+$/;


button.onclick = ()=>{
  btn.click();
}

btn.addEventListener("change", function(){
  const file = this.files[0];
  if(file){
    const reader = new FileReader();
    reader.onload = function(){
      const result = reader.result;
      img.src = result;
      wrapper.classList.add("active");
    }
    cancelBtn.addEventListener("click", function(){
      img.src = "";
      wrapper.classList.remove("active");
    })
    reader.readAsDataURL(file);
  }
  if(this.value){
    let valueStore = this.value.match(regExp);
    fileName.textContent = valueStore;
  }
});



