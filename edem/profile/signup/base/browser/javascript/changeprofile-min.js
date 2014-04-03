"use strict";jQuery.noConflict();function edem_changeprofile_init_joinable_groups(){var a=[];
var b=[];jQuery("input[name='form.joinable_groups']").each(function(c,d){cbg=jQuery("span[id=checkboxgroup-form-joinable_groups-"+c+"]");
if(jQuery(d).is(":checked")){a.push(cbg)}else{b.push(cbg)}});jQuery(b).each(function(c,d){d.detach();
jQuery("#additional-group-fields").append(d)});if(jQuery(a).length>0){jQuery("#missing-groups-message").toggle()
}}function edem_changeprofile_init_disclosure(){jQuery("#privacy-button").click(function(){var a="/support/policies/privacy/ .gs-products-gscontentmanager>:not(#tabmenu)";
jQuery("#privacy-content").load(a)})}jQuery(window).ready(function(){edem_changeprofile_init_joinable_groups();
edem_changeprofile_init_disclosure();GSSuggestFN.init("#form\\.givenName","#form\\.familyName","#form\\.fn");
var b=function(d){var c=null;var e=null;c=jQuery("#form\\.fn");e=jQuery(this);if(e.is(":checked")){c.removeAttr("disabled")
}else{c.attr("disabled","disabled")}};jQuery("#form\\.fn").attr("disabled","disabled");
jQuery("#editFnInterlock").change(b);var a=function(c){jQuery("#form\\.fn").removeAttr("disabled");
return true};jQuery("#edit-profile").submit(a);jQuery("#form\\.fn").focus()});