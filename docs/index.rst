.. Test documentation master file, created by
   sphinx-quickstart on Fri Apr 12 14:35:38 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to practice's documentation!
====================================
This is a title

Test 1
------
This is a subtitle. Need to be consistent.

The goal for this test is just to learn Sphinx

* Subtest 1: Bullet point 1. :ref:`Getting started to learn Sphnix <settingup>`
* Subtest 2: Bullet point 2

Test 2
------

**Tryit 1**
Bold text

*Try 2*
Italic

1. Sun
2. Water

Add an image below
------------------

.. figure:: shopping.webp
    :width: 400
    :scale: 50
    :align: center
    

    Figure 1. Flower

.. toctree::
   :maxdepth: 2

   Subpage/Subpages/subpage1
   Subpage/Subpages/subpage3

.. toctree::
   :maxdepth: 2
   :caption: Beginners

   subpage2

.. toctree::
   :maxdepth: 3
   :caption: Automatic API Doc Generation

   Class
   Function
   Ruonan_Li_001433201_Assignment_4



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
