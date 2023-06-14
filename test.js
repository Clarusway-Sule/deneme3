<!DOCTYPE html>
<html>
<body>
 
<p id="deneme"></p>
 <h1>hello icardi was here </h1>
<script>
var day;
switch (new Date().getDay()) {
    case 0:
        day = "Pazar";
        break;
    case 1:
        day = "Pazartesi";
        break;
    case 2:
        day = "Salı";
        break;



    
    case 3:
        day = "Çarşamba";
        break;
    case 4:
        day = "Perşembe";
        break;
    
}
document.getElementById("deneme").innerHTML = "Bugün " + day;
</script>
 
</body>
</html>