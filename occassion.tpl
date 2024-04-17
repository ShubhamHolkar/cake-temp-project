<!DOCTYPE html>
<style>
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


.home{

  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #000;
  height: 300px;
padding-bottom: 50px;
}

.home .content{
  height: 100%;
padding-top: 100px;
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

  font-family: Georgia, 'Times New Roman', Times, serif;


}
.home .content h2{
  color: white;
  text-align: center;
  justify-content: center;
  font-size: 30px;
  margin-top: 10px;;


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
  height: 980px;;
}
.products .heading{
  font-weight: bold;
  font-size: 40px;
  text-align: center;
  padding: 4rem;
}
.products .box-container{
  display: flex;
  align-items: center;
  justify-content: center;
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
  margin-left:3px ;


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
  color: rgb(17, 17, 17);
  flex-direction:row;
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
  height: 3.5rem;
  width: 15rem;
  background:var(--green);
  outline: none;
  border: .2rem solid black;
  font-size: 2rem;
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
</style>
<html lang="en" dir="ltr">

<head>
  <meta charset="utf-8">
  <title></title>
  <link rel="stylesheet" href="style.css">
  <script src="https://kit.fontawesome.com/b5a2ac3ffe.js" crossorigin="anonymous"></script>

</head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css" integrity="sha512-z3gLpd7yknf1YoNbCzqRKc4qyor8gaKU1qmn+CShxbuBusANI9QpRohGBreCFkKxLhei6S9CQXFEbbKuqLg0DA==" crossorigin="anonymous"
  referrerpolicy="no-referrer" />

<body>



  <!--- header section start --->



  <header class="header">
<img  class="logo"  src="logo1.png" alt="">
<form action="/search" method="POST">
<div class="in">
  <input type="search" class="srch" placeholder="  Search Here.." name="search">
<button  type="submit"  class="sr" name="done" value="ai"><i class="fa-solid fa-magnifying-glass" ></i></button>

</div>
</form>

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
  <section class="home" id="home">
    <div class="content">
      <h1>ARYA CAKE MAGIC</h1>
      <h2>"Crafting Sweet Moments, One Slice at a Time."</h2>


    </div>

  </section>

  <section class="products" id="products" >
    <h1 class="heading">Occasions</h1>
    <p>"Elevate Your Taste Experience with Our Exceptional Products!"</p>

    <form action="/&&" method="POST">
    <div class="box-container">



      <div class="box" >
        <img src="https://img.freepik.com/free-vector/flat-golden-circle-balloons-birthday-background_52683-34659.jpg" alt="">
        <h3>BIRTHDAY</h3>

        <button class="bt" value="v1" name="clicked">CLICK HERE </button>


      </div>
      <div class="box">
        <img src="https://www.caratlane.com/blog/wp-content/uploads/2023/08/2281A.jpg" alt="">
        <h3>ENGAGEMENT</h3>

<button class="bt" value="v2" name="clicked">CLICK HERE </button>

      </div>
      <div class="box">
        <img src="https://m.media-amazon.com/images/I/71IC2lqIgdL._AC_UF1000,1000_QL80_.jpg" alt="">
        <h3>BABY SHOWER</h3>

        <button class="bt" value="v3" name="clicked">CLICK HERE </button>

      </div>
    </div>


    <div class="box-container">


      <div class="box">
        <img src="https://m.media-amazon.com/images/I/719UlPcOU+L._AC_UF1000,1000_QL80_.jpg" alt="">
        <h3>ANNIVERSARY</h3>
          <button class="bt" value="v4" name="clicked">CLICK HERE </button>





      </div>
    </div>



</form>


  </section>


  <!---products section end ---->

  <!----we section start--->

  <section class="we" id="we">

    <h1 class="heading">"Divine Delights, Oven-Fresh Wonders!"</h1>

    <div class="we-box">


      <div class="first">
<h3>Time-Honored Goodness</h3>
<p>Our Products Are Crafted with Authentic, Home-Style Recipes, Fresh Ingredients, and Free from Preservatives or Chemicals</p>
 </div>

      <div class="second">

        <img src="https://t3.ftcdn.net/jpg/01/94/17/66/360_F_194176621_Q1aASM5s9vn6JGCi4Ob80y4lY2q8lTi2.jpg" alt="">
      </div>
      <div class="third">
        <h3>Time-Honored Goodness</h3>
        <p>Our Products Are Crafted with Authentic, Home-Style Recipes, Fresh Ingredients, and Free from Preservatives or Chemicals</p>       </div>
    </div>

    <div class="we-2">
      <div class="third">
      <h3>Time-Honored Goodness</h3>
      <p>Our Products Are makes you happy,Gives you energy,Great source of Calcium and Protien, Filled with Vitamins</p>
           </div>
  </div>
      </div>
    <button  class="btn "type="button" name="button" value="cont" name="contact">KNOW MORE </button>

  </section>
  <!---we section end--->
  <!---footer section start--->
  <section class="footer">
    <div class="box-container">
      <div class="box">
        <img src="" alt="">
       <p>Mauli Nivas,
        Samarth Nagar,
        Bhoom (near post office),
        Dharashiv</p>

      </div>
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
    <h1 class="credit">created by <span>Cake Lover</span> </h1>
  </section>



  <!---footer section end--->






</body>

</html>