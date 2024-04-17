<!DOCTYPE html>
<style>
   body {
    font-family: sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #f0f0f0;
    padding: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

header h1 {
    font-size: 2em;
    margin: 0;
}

header p {
    font-size: 1.2em;
    margin: 0;
}

.contact-info {
    display: flex;
    gap: 10px;
}

.contact-info a {
    text-decoration: none;
    color: #000;
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
nav {

    padding: 10px;
    display: flex;
    gap: 10px;
}

nav a {
    text-decoration: none;
    color: #000;
    font-weight: bold;
}

main {
    padding: 20px;
}

main h2 {
    text-align: center;
    font-size: 1.5em;
    margin-bottom: 20px;
}

.faq-item {
    margin-bottom: 15px;
}

.faq-item h3 {
    font-size: 1.2em;
    margin-bottom: 5px;
}

.faq-item p {
    font-size: 0.9em;
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

*::selection {
  background: var(--green);
  color: #fff;
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

header .help {
  font-size: 3rem;
  color: #666;
  cursor: pointer;
  display: none;
}


.home{

  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #000;
  height: 550px;
padding-bottom: 50px;
}

.home .content{
  height: 100%;
padding-top: 190px;
padding-left: 100px;
z-index: 100;
  width: 100%;
  display: flex;
  flex-direction: column;
}

.home .content h1{
  color:var(--yellow);
  font-weight: bold;
  font-size: 40px;
  text-align: center;
  justify-content: center;
  padding: .5rem;

  font-family: Georgia, 'Times New Roman', Times, serif;


}
.home .content h2{
  color: white;
  text-align: center;
  justify-content: center;
  font-size: 30px;
  margin-top: 10px;;


}


.home .content button{

  font-size: 14px;
  font-weight: 600;
  float: left;
  background-color: var(--yellow);
  font-size: 16px;
  border: 1px solid;
  border-color: #a9802a!important;
  color: black;
  border-radius: 20px;
  margin-top: 30px;
  margin-left:230px ;

  height: 60px;
width: 150px;

  text-transform: uppercase;
}

.content button:hover{

  background-color: #f9f6f6;
  color: rgb(7, 7, 7);
}
.main img{
  padding-top: 0px;
  padding-right: 100px;
  z-index: 3;
  height: 500px;
}
.main{
background-color: white;

}

.contact-banner {
  text-align: center;
  padding: 20px;
  background-color:#a9802a;
  font-size: 3rem;
}

.contact-banner h2 {
  font-size: 20px;
  margin-bottom: 10px;
  font-size: 3rem;
}

.contact-banner ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.contact-banner li {
  display: inline-block;
  margin-right: 20px;
}

.contact-banner a {
  text-decoration: none;
  color: black;
  font-size: 3rem;
  font-size: 20px;
}
</style>
<html lang="en" dir="ltr">

<head>
  <meta charset="utf-8">
  <title></title>
  <link rel="stylesheet" href="helpp.css">
  <script src="https://kit.fontawesome.com/b5a2ac3ffe.js" crossorigin="anonymous"></script>

</head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css" integrity="sha512-z3gLpd7yknf1YoNbCzqRKc4qyor8gaKU1qmn+CShxbuBusANI9QpRohGBreCFkKxLhei6S9CQXFEbbKuqLg0DA==" crossorigin="anonymous"
  referrerpolicy="no-referrer" />

<body>



  <!--- header section start --->

  <header class="header">
<img  class="logo"  src="logo1.png" alt="">

<div class="in">
  <input type="search" class="srch" placeholder="  Search Here..">
<button  type="submit"  class="sr"><i class="fa-solid fa-magnifying-glass"></i></button>
</div>

   <form action="/..." method="post">

    <nav class="navbar">

      <ul>
           <li> <a href="#products">Gallery</a></li>
        <li><button  value="log1" name="butt">Home </button> </li>
        <li><button  value="log2" name="butt">Order </button> </li>
        <li><button  value="log3" name="butt">Help </button> </li>
          <li> <button  value="log5" name="butt">login </button></li>
      </ul>

    </nav>

          </form>
  </header>


  <!---header section end--->
  <div class="help">

  </div>











  </section>
  <div class="contact-banner">
    <h2>Contact Us</h2>
    <ul>
      <li><a href="//wa.me/918767963216"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/WhatsApp.svg/2044px-WhatsApp.svg.png" width="50px" class="whatsapp_float_btn"/> </a></li>
      <li><a href="tel:+918767963216"><img src="https://banner2.cleanpng.com/20210214/wll/transparent-phone-call-icon-phone-icon-6029959676dd39.5796488816133380064869.jpg" width="40px"/></a></li>
      <li><a href="https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox"><img src="https://i.pinimg.com/736x/1e/1e/8f/1e1e8fbfed3d555c052154b6bad2c05c.jpg" width="60px"/></a></li>
    </ul>
  </div>
<!---
  <main>
    <h2>Frequently Asked Questions (FAQ)</h2>
    <section class="faq-item">
        <h3>How does it work?</h3>
        <p>anssssss</p>
    </section>
    <section class="faq-item">
        <h3>My pincode is not available, what can I do?</h3>
        <p></p>
    </section>
    <section class="faq-item">
        <h3>Is midnight delivery available?</h3>
        <p></p>
    </section>
    <section class="faq-item">
      <h3>How can i track my order?</h3>
      <p></p>
  </section>
  <section class="faq-item">
    <h3>Is there Cash on delivery available</h3>
    <p></p>
</section>
<section class="faq-item">
  <h3>How can i cancel the order?</h3>
  <p></p>
</section>
<section class="faq-item">
  <h3>Is there any discount for new customers?</h3>
  <p></p>
</section>
<section class="faq-item">
  <h3>Can i order in Advance?</h3>
  <p></p>
</section>
    </main> --->


  <!---products section end ---->

  <!----we section start--->

  <section class="we" id="we">

    <div class="we-box">

      <div class="second">

       <img src="bake.jpg" alt="">
      </div>




  </section>
  <!---we section end--->
  <!---footer section start--->
  <section class="footer">
    <div class="box-container">

      <div class="box">
        <h3 class="share">share</h3>
        <a href="#">Facebook</a>
        <a href="#">Instagram</a>

      </div>



      <div class="box">
        <h3 class="Letter">Response</h3>
        <form class="" action="index.html" method="post">
          <input type="email" placeholder="Enter your email" name="" value="">
          <button type="submit" name="button" class="fas fa-paper-plane"></button>
        </form>
      </div>

    </div>

  </section>


  <!---footer section end--->






</body>

</html>