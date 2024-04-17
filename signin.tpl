<!DOCTYPE html>
<style>
    body {
  font-family: Arial, sans-serif;
  background-color: #f1f1f1;
}

.container {
  padding: 20px;
  background-color:black;

  width: 400px;
  height: 400px;
  margin: 0 auto;
  text-align: center;
}

h1 {
  font-size: 24px;
  padding-top: 20px;
  color:#efb23f;;
}

input {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
}

button:hover {
  opacity: 1.0;
}

.terms {
  margin-top: 10px;
  color:#efb23f;
}

.terms label {
  font-size: 12px;
}

@media screen and (max-width: 300px) {
  .container {
    width: 95%;
  }
}
header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0.1rem .2rem rgba(0, 0, 0, .7);
  width: 100%;
  top: 0;
  left: 0;
  padding: 1rem 5rem;
  z-index: 1000;
  background-color: #704326;
}

header .logo  {
  height: 100px;
}


.in{
  margin-left: 180px;
  height: 30px;;
  display: flex;
  font: bold;
}
.in .srch{
  background-color: whitesmoke;


}

.in input{
  width: 300px;
   height: 50px;
   text-align:left;
   border-radius: 15px;
}

.sr:hover{
  background-color:var(--yellow);


}

.sr{
  border-radius: 10px;

  width: 80px;
  height: 50px;
}

/*
header a{
  color: var(--black);
}
header a:hover{
  color: var(--green);
}*/
header .navbar ul {
  display: flex;
  align-items: center;
  justify-content: space-between;
  list-style: none;
}

header .navbar ul li {
  margin: 0 1rem;
}

header .navbar ul li a {
  font-size: 2rem;
  color:var(--yellow);
  font-weight: 40px;
}

header .navbar ul li a:hover {
  color: white;
}

header .fa-bars {
  font-size: 3rem;
  color: #666;
  cursor: pointer;
  display: none;
}
.home{


  justify-content: center;
  align-items: center;
  background-color: #000;
  height: 700px;
  width: 1500px;
padding-bottom: 50px;
}
.main{
  background-color: #000;
  width: 100px;
  height: 100px;

  }
</style>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title></title>
  <link rel="stylesheet" href="sign.css">
  <script src="https://kit.fontawesome.com/b5a2ac3ffe.js" crossorigin="anonymous"></script>

</head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css" integrity="sha512-z3gLpd7yknf1YoNbCzqRKc4qyor8gaKU1qmn+CShxbuBusANI9QpRohGBreCFkKxLhei6S9CQXFEbbKuqLg0DA==" crossorigin="anonymous"
  referrerpolicy="no-referrer" />

<body>
</>


  <!--- header section start --->

  <header class="header">
<img  class="logo"  src="logo1.png" alt="">




    <div class="fas fa-bars">

    </div>
  </header>

  <section class="home" id="home">
    <div class="content">

              </button>
    </div>


    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sign Up</title>
        <link rel="stylesheet" href="sign.css">
    </head>
    <body>
        <div class="container">
            <h1>Sign up for a free account</h1>
            <form action="/signin" method="post">




                  <input type="email" id="email" name="email" placeholder="Enter Email" >
                <label for="psw">Password:</label>
                <input type="password" id="psw" name="passw" placeholder="Enter Password" required>

                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" placeholder="Enter Phone Number"  minlength="10"  required>

                <label for="dob">Date of Birth:</label>
                <input type="date" id="dob" name="dob" required>


                <label >Age:</label>
                 <label>Age:</label>







            <button type="submit" value="done" name="enter">Sign Up</button>

         <!---   <div class="terms">
                <label>
                    <input type="checkbox" required> I agree to the terms and conditions.
                </label>
            </div>--->
        </form>
    </div>
</body>
</html>