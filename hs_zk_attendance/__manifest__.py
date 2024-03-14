# -*- coding: utf-8 -*-
{
    'name': 'ZK-Biometric Device Integration',
    'version': '17.0.1.0.0',
    'category': 'Human Resources',
    'summary': "Integrating Biometric Device With HR Attendance (Face + Thumb)",
    'description': "Integrating Biometric Device With HR Attendance (Face + Thumb)",
    'author': 'HSxTech',
    'company': 'HSxTech',
    'maintainer': 'HSxTech',
    'website': "https://www.hsxtech.net",
    'depends': ['base_setup', 'hr_attendance'],
    'data': [
        'security/ir.model.access.csv',
        'data/cron.xml',
        'views/biometric_device_details_views.xml',
        'views/hr_employee_views.xml',
        'views/daily_attendance_views.xml',
        'views/biometric_device_attendance_menus.xml',
        'views/hs_shfits.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'images': ["static/description/zk_screenshot.jpg"],
    'auto_install': False,
    'application': True,
    'sequence': 2
}

