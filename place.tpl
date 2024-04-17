<!DOCTYPE html>
<style>
    body {
    font-family: sans-serif;
    margin: 0;
    padding: 0;
  }

  .product-container {
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 20px;
    background-color: black;
    color:  #efb23f;
    font-size: 20px;
  }

  .product-container.img {
    width: 300px;
    height: 300px;
    object-fit: cover;
  }



  .product-info {
    display: flex;
    flex-direction: column;
    width: 500px;
    justify-content: center;

  }

  .product-title {
    font-size: 24px;
    margin-bottom: 5px;
  }

  .product-rating {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
  }

  .star-rating {
    font-size: 18px;
    color: #a05827;
  }

  .review-count {
    margin-left: 5px;
    font-size: 16px;
    color: gray;
  }

  .product-price {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
  }

  .original-price {
    text-decoration: line-through;
    color: gray;
    margin-right: 5px;
  }

  .discounted-price {
    font-size: 18px;
    color: black;
  }

  .product-options {
    margin-bottom: 10px;
  }

  .product-options label {
    display: block;
    margin-bottom: 5px;
  }

  .delivery-info {
    margin-bottom: 10px;
  }

  .delivery-info p {
    margin-bottom: 5px;
  }

  #pincode {
    padding: 5px;
    border: 1px solid gray;
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
    color: yellow;
  }

  header .fa-bars {
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
    color: yellow;
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
    color: rgb(17, 17, 17);
  }
  .main img{
    padding-top: 0px;
    padding-right: 100px;
    z-index: 3;
    height: 500px;
  }
  .main{
  background-color: #000;

  }



  .products {
    background-color:var(--light);
    height: 980px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .products .heading{
    font-weight: bold;
    font-size: 40px;
    text-align: center;
    padding: 4rem;
  }
  .products .box-container{


    flex-wrap: wrap;
    padding-top: 40px;
  }

  .products .box-container .box{
    padding: 2rem 1rem;
    text-align: center;
    border: .2rem solid var(--green);
    flex:1 1 20rem;
    margin: 2rem;
    height: 300px;

  }
  .products p{
    text-align: center;

    font-size: 20px;
  }

  .products .box-container .box img{
    height: 200px;
    width: 290px;
  }
  .products .box-container .box i{
    color: var(--green);
    font-size: 4rem;

  }
  .products .box-container .box h3{
    color: black;
    font-size: 2.5rem;
  padding: 1rem 0;
  font-weight: 30px;

  }

  .products .box-container .box p{
    color: #333;
    font-size: 1.7rem;
    font-weight: 30px;

  }


  .products button{

    font-size: 13px;
    font-weight: 400;
    float: left;
    background-color: var(--yellow);
    border: 1px solid;
    border-color: #a9802a!important;
    color: black;
    border-radius: 20px;
    margin-top: 30px;
    margin-left:150px ;

    height: 40px;
  width: 100px;

    text-transform: uppercase;
    pointe0
  }

  .products button:hover{

    background-color: #f9f6f6;
    color : rgb(17, 17, 17);
  }
  .we-box {
    display: flex;
    flex-direction: row;
    align-items: center;

  }

  .we-box .second img{
    height: 500px;
    width: 600px;

  }

  .we-box h3{
    padding-top:60px ;
  font-size: 30px;

  }
  .we-box p{
  padding-top: 19px;;
    font-size: 20px;;
  }

  .we-2 h3{
    padding-top:60px ;
  font-size: 30px;

  }
  .we-2 p{
    height: 60px;
  padding-top: 19px;;
    font-size: 20px;;
  }


  .we .btn{
    position: relative;
    font-size: 14px;
    font-weight: 600;
    float: left;
    background-color: var(--yellow);
    padding: 8px 30px;
    font-size: 16px;
    border: 1px solid;
    border-color: #a9802a!important;
    color: black;
    border-radius: 20px;
    margin-bottom: 30px;
    margin-top: 30px;
    margin-left: 45%;
    text-transform: uppercase;
  }

  .we .bt{
    cursor: pointer;
    height: 4rem;
    width: 25rem;
    background:var(--green);
    outline: none;
    border: .2rem solid black;
    font-size: 7rem;
    overflow: hidden;
    z-index: 0;
    position: relative;
    color: black;
    margin: 1rem 0;
  }

  .we .btn:hover{
    color: var(--light);
    background-color: black;

  }
  .we h1{
    text-align: center;
    font-weight: bold;
    font-size: 40px;
    padding-top: 40px;
    color: var(--green);


  }




  .we {
    text-align: center;
    font-weight: bold;
    font-size: 40px;
    padding-top: 40px;
    color: var(--green);


  }
  .we-box{
    display: flex;
  }

   .we .we-box .second{
    padding-top: 10px;
  padding-left: 20px;

  }


  .footer{
    background-color: var(--light);
    margin-top: 100px;


  }
  .footer img{
  height: 100px;

  }

  .footer .box-container
  {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    width: 95%;
    margin: 0 auto;
  }
  .footer .box-container .box{
    margin: 2rem;
    flex: 1 1 25rem;
  }
  .footer .box-container .box .logo{
  font-size: 3rem;
  color: var(--green);

  }
  .footer .box-container .box p{
  font-size: 1.7rem;
  color: black;
  padding: 1rem 0;

  }

  .footer .box-container .box .share{
    text-align: center;
    font-size: 2rem;
    color: var(--green);

  }
  .footer .box-container .box:nth-child(2) a{

    text-align: center;
    font-size: 1.7rem;
    color: black;
    display: block;
    padding: .5rem 0;

  }

  .footer .box-container .box:nth-child(2) a:hover{
    color:black;
    text-decoration: underline;
  }
  .footer .box-container .box .letter{
    font-size: 3rem;
    color: black;
  }

  .footer .box-container .box form input[type="email"]{

    padding: 0 1rem;
    outline: none;
    border: 2rem solid );
    background: none;
    font-size: 1.7rem;
    color:var(--green);
    height: 4rem;
    width: 74%;


  }
  .footer .box-container .box form button{

    outline: none;
    border: none;
    background: var(--green);
    font-size: 1.9rem;
    color:black;
    height: 4rem;
    width: 25%;
    cursor: pointer;


  }


  .footer .box-container .box .Letter{
    text-align:left;
    font-size: 2rem;
    color: var(--green);
    padding-bottom: 1rem;

  }
  .product-options {
    margin-bottom: 10px;
  }

  .product-options.h2{
    display: block;
    color: #efb23f;
    margin-bottom: 5px;
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
</style>
<html lang="en" dir="ltr">

<head>
  <meta charset="utf-8">
  <title></title>
  <link rel="stylesheet" href="order.css">
  <script src="https://kit.fontawesome.com/b5a2ac3ffe.js" crossorigin="anonymous"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css" integrity="sha512-z3gLpd7yknf1YoNbCzqRKc4qyor8gaKU1qmn+CShxbuBusANI9QpRohGBreCFkKxLhei6S9CQXFEbbKuqLg0DA==" crossorigin="anonymous"
    referrerpolicy="no-referrer" />
</head>





<!--- header section start --->




<body>

  <header class="header">
    <img class="logo" src="logo1.png" alt="">

    <div class="in">
      <input type="search" class="srch" placeholder="Search Here..">
      <button type="submit" class="sr"><i class="fa-solid fa-magnifying-glass"></i></button>
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

  <div class="product-container">




<form action="/conform" method="post" enctype="multipart/form-data">
      <div class="product-options">
          <h2>Review Your Order</h2>


        <h5 style="color:white;">for Customize Cake Contact us:</h5>
        <a href="//wa.me/918767963216"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/WhatsApp.svg/2044px-WhatsApp.svg.png" width="40px" class="whatsapp_float_btn"/> </a>
         <p style="color:orange;">Customer Name:</p>
        <input  type="text" id="pincode1" placeholder="Enter Customer Name" name="name" required>

           <p style="color:orange;">Order Date:</p>
            <input type="date" id="dob" name="od" required>


        <p>Deliver To:</p>
        <input type="text" id="pincode" placeholder="Enter Address" name="address">

        <p>Upload image do you want to design on cake top :(OPTIONAL)</p>
        <br>
          <input type="file" name="image" accept="image/*">
        <p>Place Order:</p>
        <button  name="show" value="bt1">Pay Online</button>

        <button  name="show" value="bt2">Cash on Delivery</button>



      </div>
</form>

  </div>