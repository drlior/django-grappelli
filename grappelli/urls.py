# coding: utf-8

# DJANGO IMPORTS
from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('',
    
    # FOREIGNKEY & GENERIC LOOKUP
    url(r'^lookup/related/$', 'grappelli.views.related.related_lookup', name="grp_related_lookup"),
    url(r'^lookup/m2m/$', 'grappelli.views.related.m2m_lookup', name="grp_m2m_lookup"),
    url(r'^lookup/autocomplete/$', 'grappelli.views.related.autocomplete_lookup', name="grp_autocomplete_lookup"),

    # Grappelli DOM Documentation
    (r'^grp-dom-documentation/components', 'django.views.generic.simple.direct_to_template', {'template': 'grp_dom_documentation/components/components.html'}),
    (r'^grp-dom-documentation/layout-grid', 'django.views.generic.simple.direct_to_template', {'template': 'grp_dom_documentation/layout/layout_grid.html'}),
    (r'^grp-dom-documentation/layout-fluid', 'django.views.generic.simple.direct_to_template', {'template': 'grp_dom_documentation/layout/layout_fluid.html'}),
    (r'^grp-dom-documentation/layout-mueller', 'django.views.generic.simple.direct_to_template', {'template': 'grp_dom_documentation/layout/layout_mueller.html'}),
    (r'^grp-dom-documentation/layouts', 'django.views.generic.simple.direct_to_template', {'template': 'grp_dom_documentation/layout/layouts.html'}),
    (r'^grp-dom-documentation', 'django.views.generic.simple.direct_to_template', {'template': 'grp_dom_documentation/index.html'}),


    (r'^grp-doc/modules/', 'django.views.generic.simple.direct_to_template', {'template': 'grp_doc/modules.html'}),
    (r'^grp-doc/groups/', 'django.views.generic.simple.direct_to_template', {'template': 'grp_doc/groups.html'}),
    (r'^grp-doc/context-navigation/', 'django.views.generic.simple.direct_to_template', {'template': 'grp_doc/context_navigation.html'}),
    (r'^grp-doc', 'django.views.generic.simple.direct_to_template', {'template': 'grp_doc/index.html'}),
    
)
