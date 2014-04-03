"use strict";jQuery.noConflict();function gs_profile_signup_init_disclosure(){jQuery("#privacy-button").click(function(){var a="/support/policies/privacy/ .gs-products-gscontentmanager>:not(#tabmenu)";
jQuery("#privacy-content").load(a)});jQuery("#rules-button").click(function(){var a="/support/rules/ .gs-products-gscontentmanager>:not(#tabmenu)";
jQuery("#rules-content").load(a)})}function gs_profile_signup_init_webmail_check(){var a=new Array("gmail","hotmail","yahoo");
GSCheckEmailAddress.init("#form\\.email","#form\\.actions\\.register","#addressBookHelp",a,"#emailHelp")
}jQuery(window).load(function(){gs_profile_signup_init_disclosure();gsJsLoader.with_module("/++resource++check_email-20110222.js",gs_profile_signup_init_webmail_check);
jQuery("#form\\.email").focus()});