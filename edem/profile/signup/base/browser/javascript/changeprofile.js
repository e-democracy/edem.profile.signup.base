var checkedgroup = [];
var uncheckedgroup = [];

jQuery("input[name='form.joinable_groups']").each(function(index, element){
    cbg = jQuery("span[id=checkboxgroup-form-joinable_groups-"+index+"]");
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
        
jQuery(document).ready( function() {
    GSPopupFormHelp.init('#edit-profile');
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

