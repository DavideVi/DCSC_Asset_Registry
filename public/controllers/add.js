function ValidURL(str) {
  var pattern = new RegExp('(http|ftp|https)://[a-z0-9\-_]+(\.[a-z0-9\-_]+)+([a-z0-9\-\.,@\?^=%&;:/~\+#]*[a-z0-9\-@\?^=%&;/~\+#])?', 'i');
  if(!pattern.test(str)) {
    alert("Please enter a valid URL.");
    return false;
  } else {
    return true;
  }
}

$(document).ready(function() {
  $("#btn-submit").click(function(){
    var asset_name=$("#asset-name").val();
    var asset_purpose=$("#asset-purpose").val();
    var author_ids=$("#author-ids").val().split(";");
    var technologies=$("#technologies").val().split(";");
    var scm_link=$("#scm-link").val();
    var wiki_link=$("#wiki-link").val();

  $.ajax({
      url: '/api/asset/add',
      type: 'post',
      data: {
        asset_name: asset_name,
        asset_purpose: asset_purpose,
        author_ids: author_ids,
        technologies: technologies,
        stability: "0",
        scm_link: scm_link,
        wiki_link: wiki_link
      },
      headers: {
        "Content-Type": "application/json"
      },
      dataType: 'json',
      success: function (data) {
          console.info(data);
      }
  });
  });
});
