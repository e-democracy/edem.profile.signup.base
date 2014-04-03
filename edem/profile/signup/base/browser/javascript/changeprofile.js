"use strict";
jQuery.noConflict();

function edem_changeprofile_init_joinable_groups(){
    var checkedgroup = [];
    var uncheckedgroup = [];

    jQuery("input[name='form.joinable_groups']").each(function(index, element){
        var cbg = jQuery("span[id=checkboxgroup-form-joinable_groups-"+index+"]");
        if (jQuery(element).is(":checked")) {
            checkedgroup.push(cbg);
        } else {
            uncheckedgroup.push(cbg);
        }
    });

    jQuery(uncheckedgroup).each(function(index, element) {
        element.detach();
        jQuery("#additional-group-fields").append(element);
    });

    if (jQuery(checkedgroup).length > 0) {
        jQuery("#missing-groups-message").toggle();
    }
}

function edem_changeprofile_init_disclosure(){
    jQuery("#privacy-button").click( function () {
        var uri = "/support/policies/privacy/ .gs-products-gscontentmanager>:not(#tabmenu)";
        jQuery("#privacy-content").load(uri);
    });

}
        
jQuery(window).ready( function() {
    edem_changeprofile_init_joinable_groups();
    edem_changeprofile_init_disclosure();
    GSSuggestFN.init('#form\\.givenName', '#form\\.familyName', '#form\\.fn');
              
    // Handle the interlock between the FN field and the Edit checkbox
    var handle_edit_available = function(event) {
        var fnEntry = null;
        var checkbox = null;

        fnEntry = jQuery('#form\\.fn');
        checkbox = jQuery(this);

        if (checkbox.is(":checked")) {
            fnEntry.removeAttr("disabled");
        } else {
            fnEntry.attr("disabled", "disabled");
        }
    };
    jQuery('#form\\.fn').attr("disabled","disabled");
    jQuery('#editFnInterlock').change(handle_edit_available);

    var activate_fn = function(event) {
        jQuery('#form\\.fn').removeAttr("disabled"); 
        return true;
    };
    jQuery('#edit-profile').submit(activate_fn);            
    jQuery('#form\\.fn').focus();
});

