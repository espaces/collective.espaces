(function ($) {

    $(window).load(function () {

        $("button[name='form.button.DeleteComment']").on('click', function () {
            return window.confirm('Are you sure you want to delete this comment?');

        });

    });

}(jQuery));
