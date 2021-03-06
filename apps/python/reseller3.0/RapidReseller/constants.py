#!/usr/bin/python
#
# Copyright 2013 Google Inc. All Rights Reserved.

"""
      DISCLAIMER:

   (i) GOOGLE INC. ("GOOGLE") PROVIDES YOU ALL CODE HEREIN "AS IS" WITHOUT ANY
   WARRANTIES OF ANY KIND, EXPRESS, IMPLIED, STATUTORY OR OTHERWISE, INCLUDING,
   WITHOUT LIMITATION, ANY IMPLIED WARRANTY OF MERCHANTABILITY, FITNESS FOR A
   PARTICULAR PURPOSE AND NON-INFRINGEMENT; AND

   (ii) IN NO EVENT WILL GOOGLE BE LIABLE FOR ANY LOST REVENUES, PROFIT OR DATA,
   OR ANY DIRECT, INDIRECT, SPECIAL, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE
   DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, EVEN IF
   GOOGLE HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES, ARISING OUT OF
   THE USE OR INABILITY TO USE, MODIFICATION OR DISTRIBUTION OF THIS CODE OR
   ITS DERIVATIVES.
   """

__author__ = 'richieforeman@google.com (Richie Foreman)'


class ResellerProduct(object):
    GoogleApps = "Google-Apps"
    GoogleDrive = "Google-Drive-storage"
    GoogleVault = "Google-Vault"

    @classmethod
    def as_list(cls):
        return [
            cls.GoogleApps,
            cls.GoogleDrive,
            cls.GoogleVault
        ]


class ResellerSKU(object):
    '''
    A class of constants containing various Enterprise SKUs.

    src: https://developers.google.com/admin-sdk/reseller/v1/how-tos/products
    '''

    GoogleApps = "Google-Apps-For-Business"
    GoogleDriveStorage20GB = "Google-Drive-storage-20GB"
    GoogleDriveStorage50GB = "Google-Drive-storage-50GB"
    GoogleDriveStorage200GB = "Google-Drive-storage-200GB"
    GoogleDriveStorage400GB = "Google-Drive-storage-400GB"
    GoogleDriveStorage1TB = "Google-Drive-storage-1TB"
    GoogleDriveStorage2TB = "Google-Drive-storage-2TB"
    GoogleDriveStorage4TB = "Google-Drive-storage-4TB"
    GoogleDriveStorage8TB = "Google-Drive-storage-8TB"
    GoogleDriveStorage16TB = "Google-Drive-storage-16TB"
    GoogleVault = "Google-Vault"

    @classmethod
    def as_list(cls):
        return [
            cls.GoogleApps,
            cls.GoogleDriveStorage16TB,
            cls.GoogleDriveStorage1TB,
            cls.GoogleDriveStorage200GB,
            cls.GoogleDriveStorage20GB,
            cls.GoogleDriveStorage2TB,
            cls.GoogleDriveStorage400GB,
            cls.GoogleDriveStorage4TB,
            cls.GoogleDriveStorage50GB,
            cls.GoogleDriveStorage8TB,
            cls.GoogleVault
        ]


class ResellerPlanName(object):
    # As of 11/21/13, this is invalid.
    # Annual, paid every month
    #Annual = "ANNUAL"

    # Annual Prepaid for the entire year.
    AnnualYearly = "ANNUAL_YEARLY_PAY"

    # Annual paid every month.
    AnnualMonthly = "ANNUAL_MONTHLY_PAY"

    # Month-to-Month
    Flexible = "FLEXIBLE"

    # 30 Day (max) trial.
    Trial = "TRIAL"

    @classmethod
    def as_list(cls):
        return [
            cls.AnnualYearly,
            cls.AnnualMonthly,
            cls.Flexible,
            cls.Trial
        ]

class ResellerDeletionType(object):
    Cancel = "cancel"
    Downgrade = "downgrade"
    Suspend = "suspend"

class ResellerRenewalType(object):
    # automatically renew for the same license count.
    #AutoRenew = "AUTO_RENEW"

    # Auto renew with monthly pay
    AutoRenewMonthly = "AUTO_RENEW_MONTHLY_PAY"

    # auto renew with yearly pay
    AutoRenewYearly = "AUTO_RENEW_YEARLY_PAY"

    # renew current users with monthly pay
    RenewCurrentMonthly = "RENEW_CURRENT_USERS_MONTHLY_PAY"

    # renew current users with yearly pay.
    RenewCurrentYearly = "RENEW_CURRENT_USERS_YEARLY_PAY"

    # at the renewal date, switch to a "FLEXIBLE" plan type,
    # which is billed on a monthly basis.
    PayAsYouGo = "SWITCH_TO_PAY_AS_YOU_GO"

    # at the renewal date, cancel the subscription
    Cancel = "CANCEL"

    @classmethod
    def as_list(cls):
        return [
            cls.AutoRenewMonthly,
            cls.AutoRenewYearly,
            cls.RenewCurrentMonthly,
            cls.RenewCurrentYearly,
            cls.PayAsYouGo,
            cls.Cancel
        ]