


window.onkeydown=function(event){
  kc=event.keyCode;
  submit();
}

function submit(){
var d=document.getElementById("lp").value;
   if( d==="nengyuanju"||
       d ==="anjianju"||
       d ==="guangdian"||
       d ==="cishanzhongguo"||
       d ==="minzhengju"||
       d ==="jiaokeyuan"||
       d ==="guanxing"||
       d ==="xinyongzhongguo"||
       d ==="1"

   ){
      window.open({% url 'report' %});
   }
   else{
      document.getElementById("Prompt").innerHTML="拖出去斩了！！"
   }
}

function check(){
   var d=document.getElementById("lp").value;

}
