<!DOCTYPE html>
<style>
 /* Style for the dialogue box */
    #myDialog {
        width: 300px;
        padding: 20px;
        background-color: #f0f0f0;
        border: 1px solid #ccc;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        display: none;
    }

    /* Style for the button to open the dialogue box */
    #openDialogBtn {
        padding: 10px 20px;
        background-color: #007bff;
        color: #fff;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    body {
  font-family: Arial, sans-serif;
  background-color: black;
}
:root {
  --black: rgb(0, 0, 0);
  --yellow:#efb23f;
  --brown:#704326;
  --light:#E8D8C4;
}

* {
  font-family: sans-serif;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  /*  outline: none !important;
  border: none !important;*/
  text-decoration: none !important;
  text-transform: capitalize;
  transition: all .5s cubic-bezier(.37, 1.14, .26, 1.24);
}
header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  opacity 0.2;
  box-shadow: 0.1rem .2rem rgba(0, 0, 0, .7);
  width: 100%;
  top: 0;
  left: 0;
  padding: 1rem 5rem;
  z-index: 1000;
  background-color: #704326s;
}

header .logo  {
  height: 100px;
}



header .fa-bars {
  font-size: 3rem;
  color: #666;
  cursor: pointer;
  display: none;
}

*::selection {
  background: var(--green);
  color: #704326;
}

html {
  font-size: 62.5%;
  overflow-x: hidden;
  /*scroll-behavior: smooth;
  scroll-padding-top: 6.5rem;
*/
}

/*  body{
    overflow-x: hidden;
  }
*/
header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  opacity 0.2;
  box-shadow: 0.1rem .2rem rgba(0, 0, 0, .7);
  width: 100%;
  top: 0;
  left: 0;
  padding: 1rem 5rem;
  z-index: 1000;
  background-color: var(--brown);
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
  background-color: #704326;


}
.navbar button{font-size: 2rem;
    color:var(--yellow);
    font-weight: 40px;
    background-color: var(--brown);;
    display: flex;
  align-items: center;
  justify-content: space-between;
  list-style: none;
  border: none;

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
  color:#704326;
}

header .fa-bars {
  font-size: 3rem;
  color: #666;
  cursor: pointer;
  display: none;
}


.container {
  padding: 20px;
  background-color: #fff;
  border: 1px solid #ddd;
  width: 400px;
  margin-top: 90px ;
  margin-left: 530px;
  text-align: center;
}

.avatar {
  width: 100px;
  border-radius: 50%;
  margin: 0 auto;
}

h1 {
  font-size: 24px;
  padding-top: 20px;
}

input[type=email], input[type=password] {
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
  opacity: 0.8;
}

.cancelbtn {
  width: auto;
  padding: 10px 18px;
  background-color: #f44336;
}

.cancelbtn:hover {
  opacity: 0.8;
}

a {
  color: rgb(244, 245, 246);

  text-decoration: none;
  font-size: 20px;
  margin-top: 10px;

}

@media screen and (max-width: 300px) {
  .container {
    width: 95%;
  }
}

:root {
  --black: rgb(0, 0, 0);
  --yellow:#efb23f;
  --brown:#704326;
  --light:#E8D8C4;
}

* {
  font-family: sans-serif;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  /*  outline: none !important;
  border: none !important;*/
  text-decoration: none !important;
  text-transform: capitalize;
  transition: all .5s cubic-bezier(.37, 1.14, .26, 1.24);
}
header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  opacity 0.2;
  box-shadow: 0.1rem .2rem rgba(0, 0, 0, .7);
  width: 100%;
  top: 0;
  left: 0;
  padding: 1rem 5rem;
  z-index: 1000;
  background-color: #704326s;
}

header .logo  {
  height: 100px;
}



header .fa-bars {
  font-size: 3rem;
  color: #666;
  cursor: pointer;
  display: none;
}

*::selection {
  background: var(--green);
  color: #704326;
}

html {
  font-size: 62.5%;
  overflow-x: hidden;
  /*scroll-behavior: smooth;
  scroll-padding-top: 6.5rem;
*/
}

/*  body{
    overflow-x: hidden;
  }
*/
header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  opacity 0.2;
  box-shadow: 0.1rem .2rem rgba(0, 0, 0, .7);
  width: 100%;
  top: 0;
  left: 0;
  padding: 1rem 5rem;
  z-index: 1000;
  background-color: var(--brown);
}

header .logo  {
  height: 100px;
}
</style>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
    <link rel="stylesheet" href="log.css">
</head>
<body>



<header class="header">
    <img  class="logo"  src="logo1.png" alt="">




        <div class="fas fa-bars">

        </div>
      </header>


</header>



<div class="container">
    <img src="https://apps.odoo.com/web/image/loempia.module/142856/icon_image?unique=fecb0a3" alt="Login image" class="avatar">
    <h1>Login to your account</h1>
    <form action="/firstpage" method="post">
        <label for="email">Email:</label>

        <input type="email" id="email" name="email" placeholder="Enter Email" required>

        <label for="psw">Password:</label>
        <input type="password" id="psw" name="psw" placeholder="Enter Password" required>

        <button type="submit" value="log" name="loginbutton">Login</button>



      <!---  <label>
            <input type="checkbox" checked="checked" name="remember"> Remember me
        </label>--->
    </form>
            <form action="/action" method="post">
                 <h4>If you have no account Please create account.</h4>
         <button type="submit" name="signin" value="sign" >sign in</button>
                <h2 style="color:red">{{message}}</h2>

            </form>

  <!---  <a href="#">Forgot your password?</a>--->




</div>

</body>
</html>