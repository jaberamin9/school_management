var alert_items = document.querySelectorAll(".alert_item");
	var btns = document.querySelectorAll(".btn");
	var alert_wrapper = document.querySelector(".alert_wrapper");
	var close_btns = document.querySelectorAll(".close");

    alert_item.style.top = "50%";

//	btns.forEach(function(btn, btn_index){
//		btn.addEventListener("click", function(){
//			alert_wrapper.classList.add("active");
//
//			alert_items.forEach(function(alert_item, alert_index){
//				if(btn_index == alert_index){
//					alert_item.style.top = "50%";
//				}
//				else{
//					alert_item.style.top = "-100%";
//				}
//			})
//		})
//	})

	close_btns.forEach(function(close, close_index){
		close.addEventListener("click", function(){
			alert_wrapper.classList.remove("active");

			alert_items.forEach(function(alert_item, alert_index){
				alert_item.style.top = "-100%";
			})
		})
	})