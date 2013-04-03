# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from gaiatest import GaiaTestCase
from gaiatest.apps.gallery.app import Gallery
from gaiatest.apps.gallery.regions.fullscreen_image import FullscreenImage


class TestGallery(GaiaTestCase):

    def setUp(self):
        GaiaTestCase.setUp(self)

        # add photo to storage
        self.push_resource('IMG_0001.jpg', destination='DCIM/100MZLLA')

    def test_gallery_view(self):
        # https://moztrap.mozilla.org/manage/case/1326/

        gallery = Gallery(self.marionette)
        gallery.launch()
        gallery.wait_for_files_to_load(1)

        image = gallery.tap_first_gallery_item()

        self.assertIsNotNone(image.current_image_source)
        self.assertTrue(image.is_photo_toolbar_displayed)

        # Tap first image to open full screen view.
        image.tap_image()

        #self.assertIsNotNone(image.current_image_source)
        self.wait_for_condition(lambda s: self.marionette.find_element('id', 'fullscreen-view').get_attribute('class') == 'toolbarhidden')

        # TODO
        # Repeat test with landscape orientation