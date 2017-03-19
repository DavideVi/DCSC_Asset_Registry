function UserException(message, field) {
  this.message = message;
  this.field = field;
}

function ValidURL(str) {
  var pattern = new RegExp('(http|ftp|https)://[a-z0-9\-_]+(\.[a-z0-9\-_]+)+([a-z0-9\-\.,@\?^=%&;:/~\+#]*[a-z0-9\-@\?^=%&;/~\+#])?', 'i');
  if(!pattern.test(str)) {
    throw new UserException("url")
  } else {
    return str;
  }
}

function getValue(field) {
  if (field.val() === "") {
    field.parent().addClass("has-error");
    throw new UserException("")
    }
    return field.val();
  } //getValue

//when page is loaded run the function inside $(document).ready
$(document).ready(function() {
  $("#btn-submit").click(function(){
    try {
      var asset_name=getValue($("#asset-name"));
      var asset_purpose=getValue($("#asset-purpose"));
      var author_ids=getValue($("#author-ids")).split(";");
      var technologies=getValue($("#technologies")).split(";");
      var scm_link=ValidURL(getValue($("#scm-link")));
      var wiki_link=ValidURL(getValue($("#wiki-link")));

      $.ajax({
          url: '/api/asset/add',
          type: 'post',
          contentType: "application/json",
          data:  JSON.stringify({
            'asset_name': asset_name,
            'asset_purpose': asset_purpose,
            'author_ids': author_ids,
            'technologies': technologies,
            'stability': "0",
            'scm_link': scm_link,
            'wiki_link': wiki_link
          }),
          dataType: 'json',
          success: function (data) {
              console.info(data);
          }, error: function (data) {
            $("#validation-message").removeClass("hidden");
            $("#validation-message").html("Asset could not be added. Please try again later.<br/>"+data.status+"<br/>"+data.responseText);
          }
      }); //ajax
    }
    catch(e) {
      //if the exception message contains url
      //then show error message
      if (e.message.indexOf("url") > -1) {
        $("#validation-message").removeClass("hidden");
        $("#validation-message").html("URL is invalid.");
      }
      //if the exceptionmessage does not contain url
      //then show different error message
      else {
        $("#validation-message").removeClass("hidden");
        $("#validation-message").html("Field is empty.");
      }
    }
}); //button submit.click
}); //document.ready
