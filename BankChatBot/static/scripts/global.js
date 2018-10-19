(function ($) {
    'use strict';
    /*==================================================================
        [ Daterangepicker ]*/
    try {
        $('.js-datepicker').daterangepicker({
            "singleDatePicker": true,
            "showDropdowns": true,
            "autoUpdateInput": false,
            locale: {
                format: 'DD/MM/YYYY'
            },
        });
    
        var myCalendar = $('.js-datepicker');
        var isClick = 0;
    
        $(window).on('click',function(){
            isClick = 0;
        });
    
        $(myCalendar).on('apply.daterangepicker',function(ev, picker){
            isClick = 0;
            $(this).val(picker.startDate.format('DD/MM/YYYY'));
    
        });
    
        $('.js-btn-calendar').on('click',function(e){
            e.stopPropagation();
    
            if(isClick === 1) isClick = 0;
            else if(isClick === 0) isClick = 1;
    
            if (isClick === 1) {
                myCalendar.focus();
            }
        });
    
        $(myCalendar).on('click',function(e){
            e.stopPropagation();
            isClick = 1;
        });
    
        $('.daterangepicker').on('click',function(e){
            e.stopPropagation();
        });
    $('#reg_btn').on('click',function(e){
            $.ajax({
                    type: "POST",
                    url: '/registerform?fname=' + $('#first_name').val() +'&lname='+$('#last_name').val() +'&company='+$('#company').val() +'&email='+$('#email').val() +'&phone='+$('#phone').val() +'&account_type='+$('#account_type :selected').text() +'&products='+$('#products :selected').text() +'&branchs='+$('#branchs :selected').text()+'&gender='+ $('#gender :selected').text() ,
                    success: (data, status, xhr) => {

                        console.log(Date()+ "success")
                        window.location.href ='/'

                    },
                    error: (xhr, status, error) => {
                        console.log(Date() + " Question Error: " + error);
                        alert(error);
                    }
                });
        });

//$('#account_type').change(function(){
//     $prod = $('#products')
//     $("<option>Choose option</option>").append($prod);
//});
//
//var selections = {
//  "0": {
//    options: [{
//      value: 2,
//      text: "Current"
//    }, {
//      value: 3,
//      text: "Saving"
//    }, {
//      value: 4,
//      text: "Credit Card"
//    }, {
//      value: 5,
//      text: "CD"
//    }]
//  },
//  "1": {
//    options: [{
//      value: 12,
//      text: "Business account"
//    }, {
//      value: 13,
//      text: "Business account 2"
//    }, {
//      value: 14,
//      text: "Business account 3"
//    }]
//  }
//}
    
    } catch(er) {console.log(er);}
    /*[ Select 2 Config ]
        ===========================================================*/
    
    try {
        var selectSimple = $('.js-select-simple');
    
        selectSimple.each(function () {
            var that = $(this);
            var selectBox = that.find('select');
            var selectDropdown = that.find('.select-dropdown');
            selectBox.select2({
                dropdownParent: selectDropdown
            });
        });
    
    } catch (err) {
        console.log(err);
    }
    

})(jQuery);