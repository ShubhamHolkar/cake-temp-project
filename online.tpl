<!DOCTYPE html>
<style>
    *{
    margin:0;
    padding:0;
  }

  body{
    background-image: url("images/img2.jpg");
  background-size: cover;
  background-repeat: no-repeat;


  }

  .main {

    width :400px;
    margin:100px auto 0 auto;

  }
  h2{
    text-align: center;
    padding :20px;
    font-family: sans-serif;
  }

  .register{
    background-color: rgba(0,0,0,0.5);
    width:100%;
    font-size: 18px;
    border-radius: 10px;
    border:1px soid #704326(255, 255, 255, 0.3);
    box-shadow: 2px 2px 15px rgba(0,0,0,0.3);
  color: #fff;

  }
  .register{
    background-color: rgba(0, 0, 0, 0.5);
    width: 100%;
    font-size: 18px;
    border-radius: 10px;
    border: 1px soid rgba(255, 255, 255, 0.3);


    box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.3);
    color: #fff;
  }
  #register{
    margin: 40px;
  }
  label{
    font-family: sans-serif;
    font-size: 18px;
  font-style: italic;

  }

  #name{
    width: 300px
    border:1px solid #ddd;
    border-radius: 3px;
    outline: 0;
    padding: 7px;
    background-color: #fff;
    box-shadow:inset 1px 1px 5px rgba(0, 0, 0, 0.3);


  }

  #email{

      width: 300px
      border:1px solid #ddd;
      border-radius: 3px;
      outline: 0;
      padding: 7px;
      background-color: #fff;
      box-shadow:inset 1px 1px 5px rgba(0, 0, 0, 0.3);



  }

  #contact
  {

      width: 300px
      border:1px solid #ddd;
      border-radius: 3px;
      outline: 0;
      padding: 7px;
      background-color: #fff;
      box-shadow:inset 1px 1px 5px rgba(0, 0, 0, 0.3);



  }
  #address
  {

      width: 300px
      border:1px solid #ddd;
      border-radius: 3px;
      outline: 0;
      padding: 7px;
      background-color: #fff;
      box-shadow:inset 1px 1px 5px rgba(0, 0, 0, 0.3);



  }
  #rzp-button1
  {
  width:200px;
  padding: 7px;
  font-family: sans-serif;
  font-size: 18px;
  border: none;
  border-radius: 3px;
  font-weight: 600;
  background-color: rgba(250, 100, 0, 0.8);
    cursor: pointer;
    border: 1px solid rgba(255,255,255,0.3);
    box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.3);
    margin-bottom: 20px;
  }
  label,h2{
    text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.3);
  }
</style>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
<link rel="stylesheet" href="pay.css">
  </head>
  <body>

    <div class="main">
      <div class="register">
        <h2>Payment Process</h2>

        <form class="" id="register" action="index.html" method="post">
          <label for=""> Enter Full Name</label>
          <br >
          <input type="text" id="name"name=""  placeholder="full name"value="">
          <br ><br >


          <label >Enter Email</label>
          <br >
          <input type="email" id="email"name=""  placeholder="Email"value="">
          <br ><br >




<form><script src="https://checkout.razorpay.com/v1/payment-button.js" data-payment_button_id="pl_L0yz7RCedU9BGP" async> </script> </form>        </form>

      </div>



    </div>
  </body>
</html>
<script src="https://checkout.razorpay.com/v1/checkout.js"></script>
<script>
var options = {
    "key": "rzp_test_GwRA4FSgM4Ej4m", // Enter the Key ID generated from the Dashboard
    "amount": "50000", // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
    "currency": "INR",
    "name": "Acme Corp",
    "description": "Test Transaction",
    "image": "https://example.com/your_logo",
    "callback_url": "https://eneqd3r9zrjok.x.pipedream.net/",
    "prefill": {
        "name": "Gaurav Kumar",
        "email": "gaurav.kumar@example.com",
        "contact": "9999999999"
    },
    "notes": {
        "address": "Razorpay Corporate Office"
    },
    "theme": {
        "color": "#3399cc"
    }
};
var rzp1 = new Razorpay(options);
document.getElementById('rzp-button1').onclick = function(e){
    rzp1.open();
    e.preventDefault();
}
</script>