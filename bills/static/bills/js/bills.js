// Function to add another bill line
$("#add_item").click(function(){
    bill_line = "<div class='row' id='bill_items'><div class='col-12 col-md-4'><input type='text' name='description' id='description' placeholder='Description*' required minlength='3' class='form-control textInput'></div><div class='col-12 col-md-2'><input type='number' name='quantity' id='quantity' placeholder='Qty*' required class='form-control textInput quantity'></div><div class='col-12 col-md-2'><input type='number' name='price' id='price' placeholder='Price*' required class='form-control textInput price'></div><div class='col-12 col-md-2'><input type='number' name='tax' id='tax' placeholder='Tax*' required class='form-control textInput tax'></div><i class='delete_line fas fa-trash-alt delete-button'></i>"
    $("#bill_lines").append(bill_line);
});

// Function to delete bill line
$("#bill_lines").on("click", ".delete_line", function(){ 
    $(this).parent('div').remove(); 
});
