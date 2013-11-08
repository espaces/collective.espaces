Updating the theme
==================

#. Copy new resources into ``css/`` directory after building with grunt.
#. Run ``sed -i 's#../img/#../../++theme++bootstrap-framework/img/#g' bootstrap*``
   to fix image paths for icons.
#. Commit changes accordingly.
