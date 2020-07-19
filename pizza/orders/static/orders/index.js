const toppingTemplate = Handlebars.compile(document.querySelector('#topping').innerHTML);
const addonTemplate = Handlebars.compile(document.querySelector('#addon').innerHTML);

document.addEventListener('DOMContentLoaded', ()=>{
  document.querySelectorAll(".product").forEach(p =>{
    p.onclick = () =>{
      get_product(p.dataset.product);
    }
  })
});


function get_product(product_id){
  const request = new XMLHttpRequest();
  request.open("GET", `products/${product_id}`);

  request.onload = () => {
    const data = JSON.parse(request.responseText);
    console.log(data)
    document.querySelector("#product-name").innerHTML = data.name + " - " + data.category;
    document.querySelector("#product-description").innerHTML = data.description;
    document.querySelector("#product-small-price").innerHTML = "Small $" + data.smallPrice;
    document.querySelector("#product-large-price").innerHTML = "Large $" + data.largePrice;
    let toppingsSection = document.querySelector('#toppings');
    toppingsSection.innerHTML = "";
    data.toppings.forEach(t =>{
      const topping = toppingTemplate({"id":t.id, "name":t.name});
      toppingsSection.innerHTML += topping;
    });
  }

  request.send();
}
