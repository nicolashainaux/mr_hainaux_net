// IIFE - Immediately Invoked Function Expression
(function(does_the_job) {

    // The global jQuery object is passed as a parameter
    does_the_job(window.jQuery, window, document);

}(function($, window, document) {

    // The $ is now locally scoped

    // Listen for the jQuery ready event on the document
    $(function() {
        // The DOM is ready!

        $('main').on("click", ".btn-mm", function() {
            // this.preventDefault();
            var url = this.href
            $.get(this.href, function () {
                var request = new XMLHttpRequest();
                request.open("GET", url, true);
                request.responseType = "blob";
                request.onload = function (e) {
                    if (this.status === 200) {
                        // `blob` response
                        console.log(this.response);
                        // create `objectURL` of `this.response` : `.pdf` as `Blob`
                        var file = window.URL.createObjectURL(this.response);
                        var a = document.createElement("a");
                        a.href = file;
                        a.download = this.response.name || "detailPDF";
                        document.body.appendChild(a);
                        a.click();
                        // remove `a` following `Save As` dialog,
                        // `window` regains `focus`
                        window.onfocus = function () {
                           document.body.removeChild(a)
                        }
                    };
                };
                request.send();
            });

        });

    });

    // The rest of the code goes here!

}));