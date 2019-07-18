
  function validate(){

      var password = document.getElementById("1stpass").value;
      var confirmPassword = document.getElementById("confirmpass").value;
      if(password != confirmPassword){
        alert("password dosent match. Try again!");
        return false;

      }
      return true;


    }
