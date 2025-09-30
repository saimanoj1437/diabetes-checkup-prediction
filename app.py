<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"/>

    

    
</head>
<body>
   
    <div class="container p-4">
        <div> 
            <form id="customerform">

                <div class="row mb-3">

                    <label for="name" class="col-sm-3 col-form-label">Full Name</label>

                    <div class="col-sm-9">

                      <input type="text" class="form-control" id="name" placeholder="Enter Name" required>
                    </div>

                  </div>
                  <div class="row mb-3">
                    <label for="email" class="col-sm-3 col-form-label">Email</label>
                    
                    <div class="col-sm-9">
                      <input type="email" class="form-control" id="email" placeholder="Enter mail" required>
                    </div>
                  </div>
            
                  
                  <div class="row mb-3">
                    <label for="contact" class="col-sm-3 col-form-label">Contact no:</label>
                    <div class="col-sm-9">
                      <input type="text" class="form-control" id="contact" placeholder="Enter Contact no" required>
                    </div>
                  </div>

                  <div class="row mb-3">
                    
                    <label class="col-sm-3 col-form-label" for="accounttype"> Account Type:</label>
                    <div class="col-sm-9">
                        <select class="form-select" id="accounttype" required>
                            <option value="">Select account type</option>
                            <option value="savings">savings</option>
                            <option value="current">current</option>
                        </select>
                    </div>
                  
                  </div>

                  <div class="mb-3 row">
                    <div class="col-sm-10 offset-sm-3">
                      <button type="submit" class="btn btn-primary">Add Customer</button>
                    </div>

                    

                  </div>
                  
                  
                         
            </form>


            <h3 class="mt-5">Customer List</h3>
            <div class="table-r">
              <table class="table table-bordered mt-3" id="customerTable">
                <tbody class="table-light">
                  <tr>
                    <td>Name:</td>
                    <td>Email:</td>
                    <td>Contact</td>
                    <td>Account Type:</td>
                  </tr>


                </tbody>
              </table>
            </div>

        </div>

        <script src="bootstrap.js"></script>


    
</body>
</html>


















document.addEventListener("DOMContentLoaded",()=> {

    const form = document.getElementById("customerform");

    const customerTable = document.querySelector("#customerTable tbody");

    form.addEventListener("submit",function (e) {

        e.preventDefault();

        const name = document.getElementById("name").value;
        const email = document.getElementById("email").value;
        const contact = document.getElementById("contact").value;
        const accounttype = document.getElementById("accounttype").value;


        const newrow = document.createElement("tr");

        newrow.innerHTML = `
        <td>${name}</td>
        <td>${email}</td>
        <td>${contact}</td>
        <td>${accounttype}</td> `;


        customerTable.appendChild(newrow);
        form.reset();


    });

    

});
