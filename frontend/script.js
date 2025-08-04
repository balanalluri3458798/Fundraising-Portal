fetch("http://127.0.0.1:5000/api/user")
  .then(response => response.json())
  .then(data => {
    document.getElementById("name").textContent = data.name;
    document.getElementById("code").textContent = data.referral_code;
    document.getElementById("amount").textContent = data.donation_amount;
  })
  .catch(error => {
    console.error("Error fetching data:", error);
  });
