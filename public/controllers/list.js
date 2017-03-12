$(document).ready(function() {
  $.ajax({
      url: '/api/list',
      type: 'get',
      contentType: "application/json",
      dataType: 'json',
      success: function (data) {
          console.info(data);
          for (var asset_index in data) {
              $("#asset-list").html($("#asset-list").html()+
              '<div class="panel panel-default"><div class="panel-body result"><div style="color: orange; font-size: 14pt" class="pull-right"><span class="glyphicon glyphicon-star"></span><span class="glyphicon glyphicon-star"></span><span class="glyphicon glyphicon-star"></span><span class="glyphicon glyphicon-star-empty"></span><span class="glyphicon glyphicon-star-empty"></span></div><h3><span>'+data[asset_index].asset_name+'</span><small><div style="margin-left: 5px" class="label label-danger"></div></small></h3><div class="help-block">asset_purpose</div><div style="margin-right: 5px" class="label label-success">technologies</div></div></div>'
          );
        }
      },
      error: function(data) {
         console.info(data);
      }
  });
});
