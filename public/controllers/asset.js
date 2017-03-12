$(document).ready(function() {
  $.ajax({
      url: '/api/asset/get/' + asset_id,
      type: 'get',
      contentType: "application/json",
      dataType: 'json',
      success: function (data) {
          console.info(data);
          $("#asset-name").html(data.asset_name);
          $("#author-ids").html(data.author_ids);
          $("#asset-purpose").html(data.asset_purpose);
          $("#stability").html(data.stability);
          $("#technologies").html(data.technologies);
          $("#scm-link").attr("href", data.scm_link);
          $("#wiki-link").attr("href", data.wiki_link);
      },
      error: function(data) {
         console.info(data);
      }
  });
});
