

//scroll

$(window).scroll(function(){
    if ($(this).scrollTop() > 100) {
        event.preventDefault();
        $(".scrollToTop").css({'transform': 'translate(0px, 0px)'});
    } else {
        $(".scrollToTop").css({'transform': 'translate(80px, 0px)'});
    }
});

$('.scrollToTop').click(function(){
    $('html, body').animate({scrollTop : 0},800);
    return false;
});

$.fn.scrollEnd = function(callback, timeout) {
    $(this).scroll(function(){
        var $this = $(this);
        if ($this.data('scrollTimeout')) {
            clearTimeout($this.data('scrollTimeout'));
        }
        $this.data('scrollTimeout', setTimeout(callback,timeout));
    });
};
//If the function has stopped, we hide the scroll btn
$(window).scrollEnd(function(){
    $(".scrollToTop").css({'transform': 'translate(80px, 0px)'});
}, 1500);



$(function() {
    $('.scroll-down').click (function() {
        $('html, body').animate({scrollTop: $('colwall').offset().top }, 'slow');
        return false;
    });
});







