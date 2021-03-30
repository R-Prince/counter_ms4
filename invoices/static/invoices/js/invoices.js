// Function to add another invoice line
$("#add_item").click(function(){
    invoice_line = "<div class='row' id='invoice_items'><div class='col-12 col-md-4'><input type='text' name='description' id='description' placeholder='Description*' required minlength='3' class='form-control textInput'></div><div class='col-12 col-md-2'><input type='number' name='quantity' id='quantity' placeholder='Qty*' required class='form-control textInput quantity'></div><div class='col-12 col-md-2'><input type='number' name='price' id='price' placeholder='Price*' required class='form-control textInput price'></div><div class='col-12 col-md-2'><input type='number' name='tax' id='tax' placeholder='Tax*' required class='form-control textInput tax'></div><i class='delete_line fas fa-trash-alt delete-button'></i>"
    $("#invoice_lines").append(invoice_line);
});

// Function to delete invoice line
$("#invoice_lines").on("click", ".delete_line", function(){ 
    $(this).parent('div').remove(); 
});
