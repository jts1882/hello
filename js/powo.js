function initialise() {
     
  var output = "initialise test programme";
  //alert(output);   
  $('#content1').html(output);
  
  loadPython();
}
function loadPython() {          
   
   var url = "powo.py";
   url = "testpython.py";
   //url = "testPykew.py";
   
   $.ajax({
       url: url,
       type: 'GET',
       data: { param: "text"},
       success: function (response) {
           console.log(response);
           var html = '<iframe id="TestiFrame" title="Test iFrame">' +response +'</iframe>'; 
           $("#content").html(html);
       },
       error: function (error) {
           console.log(error);
       }
    });
}
