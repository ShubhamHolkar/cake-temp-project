<!DOCTYPE html>
<html lang="en">
<style>
    body {
  font-family: sans-serif;
  margin: 0;
  padding: 0;
}

header {
  text-align: center;
  padding: 20px;
}

main {
  padding: 20px;
}

p {
  margin-bottom: 10px;
}

a {
  text-decoration: none;
  color: #007bff;
}

footer {
  display:flex;
  text-align: center;
  padding: 20px;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

footer a{
  color: black;
}
footer button{

  font-size: 14px;
  font-weight: 600;
  float: left;
  background-color: #a9802a;
  font-size: 16px;
  border: 1px solid;
  border-color: #a9802a!important;

  border-radius: 20px;
  margin-top: 30px;



  height: 60px;
width: 150px;

  text-transform: uppercase;
}
</style>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Order Confirmation</title>
  <link rel="stylesheet" href="ab.css">
</head>
<body>
  <header>
    <h1>Order Successfully Placed</h1>
    <IMG SRC="https://i.gifer.com/7efs.gif">.
  </header>

  <footer>
    <form action="/thank" method= post>
    <h1>THANK YOU FOR ORDER</h1>
    <button name="thank" value="you" >See More</button>
 </form>
  </footer>

</body>
</html>