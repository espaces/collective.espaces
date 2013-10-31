.. contents::

Introduction
============

Policy and site configuration for an `eSpaces` project site.

Essentially, this is an opinionated configuration for usage of
`collective.spaces <https://github.com/collective/collective.spaces>`_,
featuring a dependency on a number of well-worn add-ons for Plone,
several security customisations, and various other configuration items
as listed in the features below.

Features
========

* Self-creation of eSpaces (powered by `collective.spaces`)

  * Users must be authenticated via Shibboleth (AAF) to be able to create
    their own Spaces. This is protected by a special Plone security
    role that this policy product assigns to "AAF Authenticated" users.
  * Any user with an AAF account is able to create a Space.
  * File quotas are limited to 100MB per file, and 20MB per image.
  * Ability to associate a custom URL with your space, or the ability
    to have your own *.espaces.edu.au domain.
  * Customisable theme per-Space (via Diazo and plone.app.theming)

* Flexible management and customisation

  * Self-management of access and configuration of Space owners.
  * Customisable look and feel with ability to select a logo and a theme
    from a pre-set number of options.
  * Customisable navigation and portlets (Twitter, RSS, news and events,
    custom text, and more).
    
* Flexible authentication

  * Login via Shibboleth and the Australian Access Federation (AAF) for
    researchers and collaborators.
  * Self-registration enabled for non-AAF users.

Final customisations
====================

* Mailhost settings (mailhost.xml)
* Site email address (properties.xml)
* Analytics via webstats_js property (propertiestool.xml)

Future
======

* Ability to share content with the world via RSS feeds
  (see aws.authrss for token-based secure access)
* Quotas on a per-Space basis.

  * Look at ftw.quota and Products.Quota for implementation details
    to borrow.

* Display size quota usage in a portlet or somewhere accessible to the user.
* Potentially limits on the number of Spaces a person may create

