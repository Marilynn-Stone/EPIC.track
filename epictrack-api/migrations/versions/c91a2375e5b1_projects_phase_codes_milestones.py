"""projects, phase_codes, milestones

Revision ID: c91a2375e5b1
Revises: 411ca8b6d6d8
Create Date: 2022-06-27 13:20:44.699199

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import column, table


# revision identifiers, used by Alembic.
revision = 'c91a2375e5b1'
down_revision = '411ca8b6d6d8'
branch_labels = None
depends_on = None


def upgrade():
    #phase codes
    op.execute('TRUNCATE phase_codes RESTART IDENTITY CASCADE')
    op.drop_column('phase_codes', 'start_event')
    op.drop_column('phase_codes', 'end_event')
    
    milestone_type = table('milestone_types',
                    column('id',sa.Integer),
                    column('name',sa.String))
    op.bulk_insert(milestone_type,
        [{
            'name': 'PECP Close'
        }]
    )
    phase_code = table('phase_codes',
                    column('sort_order',sa.Integer),
                    column('work_type_id',sa.Integer),
                    column('ea_act_id',sa.Integer),
                    column('duration',sa.Integer),
                    column('legislated',sa.Boolean),
                    column('color',sa.String),
                    column('name',sa.String))
    op.bulk_insert(
        phase_code,
        [{
            'sort_order': 1,
            'name': 'Early Engagement',
            'work_type_id': 6,
            'duration': 90,
            'legislated': True,
            'ea_act_id': 3,
            'color': '#E1EBF3'
        },{
            'sort_order': 2,
            'name': 'Proponent Time: Early Engagement',
            'work_type_id': 6,
            'duration': 365,
            'legislated': False,
            'ea_act_id': 3,
            'color': '#CCFFFF'
        },{
            'sort_order': 3,
            'name': 'Readiness Decision',
            'work_type_id': 6,
            'duration': 60,
            'legislated': False,
            'ea_act_id': 3,
            'color': '#C3D7E8'
        }, {
            'sort_order': 4,
            'name': 'Process Planning',
            'work_type_id': 6,
            'duration': 120,
            'legislated': True,
            'ea_act_id': 3,
            'color': '#A6C3DD'
        }, {
            'sort_order': 5,
            'name': 'Proponent Time: Process Planning',
            'work_type_id': 6,
            'duration': 1095,
            'legislated': False,
            'ea_act_id': 3,
            'color': '#CCFFFF'
        }, {
            'sort_order': 6,
            'name': 'Application Development & Review',
            'work_type_id': 6,
            'duration': 180,
            'legislated': True,
            'ea_act_id': 3,
            'color': '#FAEADC'
        }, {
            'sort_order': 7,
            'name': 'Proponent Time: Application Review',
            'work_type_id': 6,
            'duration': 365,
            'legislated': False,
            'ea_act_id': 3,
            'color': '#CCFFFF'
        }, {
            'sort_order': 8,
            'name': 'Effects Assessment/Recommentations',
            'work_type_id': 6,
            'duration': 150,
            'legislated': True,
            'ea_act_id': 3,
            'color': '#F6D5B9'
        }, {
            'sort_order': 10,
            'name': 'Referral/Decision',
            'work_type_id': 6,
            'duration': 30,
            'legislated': True,
            'ea_act_id': 3,
            'color': '#F2C096'
        }])
   
    op.execute('TRUNCATE milestones RESTART IDENTITY CASCADE')
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('milestones', sa.Column('start_at', sa.Integer(), nullable=False))
    op.add_column('milestones', sa.Column('duration', sa.Integer(), nullable=False))
    op.add_column('milestones', sa.Column('kind', sa.String(), nullable=False))
    op.add_column('milestones', sa.Column('auto', sa.Boolean(), nullable=True))
    op.drop_column('milestones', 'is_end_event')
    op.drop_column('milestones', 'is_start_event')
    milestone = table('milestones', 
                        column('name',sa.String),
                        column('phase_id',sa.Integer),
                        column('milestone_type_id',sa.Integer),
                        column('sort_order',sa.Integer),
                        column('start_at',sa.Integer),
                        column('duration',sa.Integer),
                        column('kind',sa.String),
                        column('auto',sa.Boolean))
    op.bulk_insert(milestone,
    [
    {
        "name": "Accept IPD & Engagement Plan",
        "phase_id": 1,
        "milestone_type_id": 16,
        "sort_order": 1,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": True
    },
    {
        "name": "IPD Accepted Announcement & Tweet",
        "phase_id": 1,
        "milestone_type_id": 5,
        "sort_order": 2,
        "start_at": 0,
        "duration": 0,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "PECP Coming Announcement & Tweet",
        "phase_id": 1,
        "milestone_type_id": 5,
        "sort_order": 3,
        "start_at": 7,
        "duration": 0,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "PECP",
        "phase_id": 1,
        "milestone_type_id": 11,
        "sort_order": 4,
        "start_at": 14,
        "duration": 30,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "PECP Open Announcement & Tweet",
        "phase_id": 1,
        "milestone_type_id": 5,
        "sort_order": 5,
        "start_at": 14,
        "duration": 0,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "PECP Closing Announcement & Tweet",
        "phase_id": 1,
        "milestone_type_id": 5,
        "sort_order": 6,
        "start_at": 42,
        "duration": 0,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "PECP Close",
        "phase_id": 1,
        "milestone_type_id": 18,
        "sort_order": 7,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Format SoE",
        "phase_id": 1,
        "milestone_type_id": 15,
        "sort_order": 8,
        "start_at": 68,
        "duration": 0,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "PECP",
        "phase_id": 1,
        "milestone_type_id": 11,
        "sort_order": 9,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Open House",
        "phase_id": 1,
        "milestone_type_id": 6,
        "sort_order": 10,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Virtual Open House",
        "phase_id": 1,
        "milestone_type_id": 17,
        "sort_order": 11,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Project Withdrawn",
        "phase_id": 1,
        "milestone_type_id": 1,
        "sort_order": 12,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Other",
        "phase_id": 1,
        "milestone_type_id": 8,
        "sort_order": 13,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Summary of Engagement Announcement & Tweet",
        "phase_id": 1,
        "milestone_type_id": 5,
        "sort_order": 14,
        "start_at": 90,
        "duration": 0,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "Summary of Engagement",
        "phase_id": 1,
        "milestone_type_id": 13,
        "sort_order": 15,
        "start_at": 90,
        "duration": 0,
        "kind": "EVENT",
        "auto": True
    },
    {
        "name": "Start of Proponent Time: Early Engagement",
        "phase_id": 2,
        "milestone_type_id": 12,
        "sort_order": 16,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": True
    },
    {
        "name": "Project Termination (s.39)",
        "phase_id": 2,
        "milestone_type_id": 1,
        "sort_order": 17,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Other",
        "phase_id": 2,
        "milestone_type_id": 8,
        "sort_order": 18,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "End of Proponent Time: Early Engagement",
        "phase_id": 2,
        "milestone_type_id": 12,
        "sort_order": 19,
        "start_at": 365,
        "duration": 0,
        "kind": "EVENT",
        "auto": True
    },
    {
        "name": "Accept Detailed Project Description",
        "phase_id": 3,
        "milestone_type_id": 16,
        "sort_order": 20,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": True
    },
    {
        "name": "DPD Accepted Announcement & Tweet",
        "phase_id": 3,
        "milestone_type_id": 5,
        "sort_order": 21,
        "start_at": 0,
        "duration": 0,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "Referred to Minister for Decision",
        "phase_id": 3,
        "milestone_type_id": 13,
        "sort_order": 22,
        "start_at": 30,
        "duration": 0,
        "kind": "EVENT",
        "auto": True
    },
    {
        "name": "Referred to Minister Announcement & Tweet",
        "phase_id": 3,
        "milestone_type_id": 5,
        "sort_order": 23,
        "start_at": 30,
        "duration": 0,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "Other",
        "phase_id": 3,
        "milestone_type_id": 8,
        "sort_order": 24,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Minister's Decision Announcement & Tweet",
        "phase_id": 3,
        "milestone_type_id": 5,
        "sort_order": 25,
        "start_at": 60,
        "duration": 0,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "Ministers Decision",
        "phase_id": 3,
        "milestone_type_id": 4,
        "sort_order": 26,
        "start_at": 60,
        "duration": 0,
        "kind": "EVENT",
        "auto": True
    },
    {
        "name": "Start of the Process Planning Phase",
        "phase_id": 4,
        "milestone_type_id": 16,
        "sort_order": 27,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": True
    },
    {
        "name": "PECP Coming Announcement & Tweet",
        "phase_id": 4,
        "milestone_type_id": 5,
        "sort_order": 28,
        "start_at": 52,
        "duration": 0,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "PECP",
        "phase_id": 4,
        "milestone_type_id": 11,
        "sort_order": 29,
        "start_at": 60,
        "duration": 30,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "PECP Open Announcement & Tweet",
        "phase_id": 4,
        "milestone_type_id": 5,
        "sort_order": 20,
        "start_at": 60,
        "duration": 0,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "PECP Closing Announcement & Tweet",
        "phase_id": 4,
        "milestone_type_id": 5,
        "sort_order": 31,
        "start_at": 88,
        "duration": 0,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "PECP Close",
        "phase_id": 4,
        "milestone_type_id": 18,
        "sort_order": 32,
        "start_at": 90,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "PECP",
        "phase_id": 4,
        "milestone_type_id": 11,
        "sort_order": 33,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Open House",
        "phase_id": 4,
        "milestone_type_id": 6,
        "sort_order": 34,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Virtual Open House",
        "phase_id": 4,
        "milestone_type_id": 17,
        "sort_order": 35,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Project Withdrawn",
        "phase_id": 4,
        "milestone_type_id": 1,
        "sort_order": 36,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Other",
        "phase_id": 4,
        "milestone_type_id": 8,
        "sort_order": 37,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Process Order Announcement & Tweet",
        "phase_id": 4,
        "milestone_type_id": 5,
        "sort_order": 38,
        "start_at": 120,
        "duration": 0,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "Process Order Issued",
        "phase_id": 4,
        "milestone_type_id": 7,
        "sort_order": 39,
        "start_at": 120,
        "duration": 0,
        "kind": "EVENT",
        "auto": True
    },
    {
        "name": "Start of Proponent Time: Process Planning",
        "phase_id": 5,
        "milestone_type_id": 12,
        "sort_order": 40,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": True
    },
    {
        "name": "Project Termination (s.39)",
        "phase_id": 5,
        "milestone_type_id": 1,
        "sort_order": 41,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Process Order Amended (s.19)",
        "phase_id": 5,
        "milestone_type_id": 7,
        "sort_order": 42,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Other",
        "phase_id": 5,
        "milestone_type_id": 8,
        "sort_order": 43,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "End of Proponent Time: Process Planning",
        "phase_id": 5,
        "milestone_type_id": 12,
        "sort_order": 44,
        "start_at": 1095,
        "duration": 0,
        "kind": "EVENT",
        "auto": True
    },
    {
        "name": "Accept EAC Application",
        "phase_id": 6,
        "milestone_type_id": 16,
        "sort_order": 45,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": True
    },
    {
        "name": "Application Accepted Announcement & Tweet",
        "phase_id": 6,
        "milestone_type_id": 5,
        "sort_order": 46,
        "start_at": 0,
        "duration": 0,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "PECP Coming Announcement & Tweet",
        "phase_id": 6,
        "milestone_type_id": 5,
        "sort_order": 47,
        "start_at": 7,
        "duration": 0,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "PECP",
        "phase_id": 6,
        "milestone_type_id": 11,
        "sort_order": 48,
        "start_at": 14,
        "duration": 30,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "PECP Open Announcement & Tweet",
        "phase_id": 6,
        "milestone_type_id": 5,
        "sort_order": 49,
        "start_at": 14,
        "duration": 0,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "PECP Closing Announcement & Tweet",
        "phase_id": 6,
        "milestone_type_id": 5,
        "sort_order": 50,
        "start_at": 44,
        "duration": 0,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "PECP Close",
        "phase_id": 6,
        "milestone_type_id": 18,
        "sort_order": 51,
        "start_at": 45,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "PECP",
        "phase_id": 6,
        "milestone_type_id": 11,
        "sort_order": 52,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Open House",
        "phase_id": 6,
        "milestone_type_id": 6,
        "sort_order": 53,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Virtual Open House",
        "phase_id": 6,
        "milestone_type_id": 17,
        "sort_order": 54,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Process Order Amended (s.19)",
        "phase_id": 6,
        "milestone_type_id": 7,
        "sort_order": 55,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Project Withdrawn",
        "phase_id": 6,
        "milestone_type_id": 1,
        "sort_order": 56,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Other",
        "phase_id": 6,
        "milestone_type_id": 8,
        "sort_order": 57,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "EAC Application Notice Announcement & Tweet",
        "phase_id": 6,
        "milestone_type_id": 5,
        "sort_order": 58,
        "start_at": 180,
        "duration": 0,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "EAC Application Notice Posted",
        "phase_id": 6,
        "milestone_type_id": 13,
        "sort_order": 59,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": True
    },
    {
        "name": "Start of Proponent Time: Application Review",
        "phase_id": 7,
        "milestone_type_id": 12,
        "sort_order": 60,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": True
    },
    {
        "name": "Project Termination (s.39)",
        "phase_id": 7,
        "milestone_type_id": 1,
        "sort_order": 61,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Process Order Amended (s.19)",
        "phase_id": 7,
        "milestone_type_id": 7,
        "sort_order": 62,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Other",
        "phase_id": 7,
        "milestone_type_id": 8,
        "sort_order": 63,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "End of Proponent Time: Application Review",
        "phase_id": 7,
        "milestone_type_id": 12,
        "sort_order": 64,
        "start_at": 365,
        "duration": 0,
        "kind": "EVENT",
        "auto": True
    },
    {
        "name": "Accept Revised EAC Application",
        "phase_id": 8,
        "milestone_type_id": 16,
        "sort_order": 65,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": True
    },
    {
        "name": "Revised Application Accepted Announcement & Tweet",
        "phase_id": 8,
        "milestone_type_id": 5,
        "sort_order": 66,
        "start_at": 0,
        "duration": 0,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "Draft Assessment Report Posted",
        "phase_id": 8,
        "milestone_type_id": 13,
        "sort_order": 67,
        "start_at": 90,
        "duration": 0,
        "kind": "EVENT",
        "auto": True
    },
    {
        "name": "PECP Coming Announcement & Tweet",
        "phase_id": 8,
        "milestone_type_id": 5,
        "sort_order": 68,
        "start_at": 97,
        "duration": 0,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "PECP",
        "phase_id": 8,
        "milestone_type_id": 11,
        "sort_order": 69,
        "start_at": 104,
        "duration": 30,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "PECP Open Announcement & Tweet",
        "phase_id": 8,
        "milestone_type_id": 5,
        "sort_order": 70,
        "start_at": 104,
        "duration": 0,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "PECP Closing Announcement & Tweet",
        "phase_id": 8,
        "milestone_type_id": 5,
        "sort_order": 71,
        "start_at": 132,
        "duration": 0,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "PECP Close",
        "phase_id": 8,
        "milestone_type_id": 18,
        "sort_order": 72,
        "start_at": 134,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Process Order Amended (s.19)",
        "phase_id": 8,
        "milestone_type_id": 7,
        "sort_order": 73,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Project Withdrawn",
        "phase_id": 8,
        "milestone_type_id": 1,
        "sort_order": 74,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Other",
        "phase_id": 8,
        "milestone_type_id": 8,
        "sort_order": 75,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Referral Announcement & Tweet",
        "phase_id": 8,
        "milestone_type_id": 5,
        "sort_order": 76,
        "start_at": 150,
        "duration": 0,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "Open House",
        "phase_id": 8,
        "milestone_type_id": 6,
        "sort_order": 77,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Virtual Open House",
        "phase_id": 8,
        "milestone_type_id": 17,
        "sort_order": 78,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": False
    },
    {
        "name": "Referral Package Sent to Ministers",
        "phase_id": 8,
        "milestone_type_id": 14,
        "sort_order": 77,
        "start_at": 150,
        "duration": 0,
        "kind": "EVENT",
        "auto": True
    },
    {
        "name": "Refered to Ministers",
        "phase_id": 9,
        "milestone_type_id": 13,
        "sort_order": 80,
        "start_at": 0,
        "duration": 0,
        "kind": "EVENT",
        "auto": True
    },
    {
        "name": "Meeting with Ministers",
        "phase_id": 9,
        "milestone_type_id": 3,
        "sort_order": 81,
        "start_at": 7,
        "duration": 0,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "EAC Decision Announcement & Tweet",
        "phase_id": 9,
        "milestone_type_id": 5,
        "sort_order": 82,
        "start_at": 30,
        "duration": 0,
        "kind": "ENGAGEMENT",
        "auto": True
    },
    {
        "name": "Minister's EAC Decision",
        "phase_id": 9,
        "milestone_type_id": 4,
        "sort_order": 83,
        "start_at": 30,
        "duration": 0,
        "kind": "EVENT",
        "auto": True
    }
    ])
    
    op.add_column('projects', sa.Column('abbreviation', sa.String(length=10), nullable=True))
    outcome = table('outcomes',
                column('id',sa.Integer),
                column('name',sa.String),
                column('milestone_id',sa.Integer),
                column('sort_order',sa.Integer),
                column('terminates_work',sa.Boolean))
    op.bulk_insert(outcome,
    [{
        'name': 'Project Withdrawn',
        'milestone_id': 12,
        'sort_order': 1,
        'terminates_work': True
    },{
        'name': 'Project Termination',
        'milestone_id': 17,
        'sort_order': 2,
        'terminates_work': False
    },{
        'name': 'Revised DPD Ordered',
        'milestone_id': 26,
        'sort_order': 3,
        'terminates_work': False
    },{
        'name': 'Exemption Order Granted',
        'milestone_id': 26,
        'sort_order': 4,
        'terminates_work': False
    },{
        'name': 'Assessment Terminated',
        'milestone_id': 26,
        'sort_order': 5,
        'terminates_work': True
    },{
        'name': 'Project Enters the EA Process',
        'milestone_id': 26,
        'sort_order': 6,
        'terminates_work': False
    },{
        'name': 'Project Withdrawn',
        'milestone_id': 36,
        'sort_order': 7,
        'terminates_work': True
    },{
        'name': 'Project Termination',
        'milestone_id': 41,
        'sort_order': 8,
        'terminates_work': False
    },{
        'name': 'Project Withdrawn',
        'milestone_id': 56,
        'sort_order': 9,
        'terminates_work': True
    },{
        'name': 'Project Termination',
        'milestone_id': 61,
        'sort_order': 10,
        'terminates_work': False
    },{
        'name': 'Project Withdrawn',
        'milestone_id': 74,
        'sort_order': 11,
        'terminates_work': True
    },{
        'name': 'EAC Granted',
        'milestone_id': 83,
        'sort_order': 12,
        'terminates_work': False
    },{
        'name': 'EAC Refused',
        'milestone_id': 83,
        'sort_order': 13,
        'terminates_work': False
    }])
    # ### end Alembic commands ###


def downgrade():
    op.add_column('phase_codes', sa.Column('end_event', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('phase_codes', sa.Column('start_event', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.execute('TRUNCATE phase_codes RESTART IDENTITY  CASCADE')
    op.execute('ALTER SEQUENCE phase_codes_id_seq RESTART WITH 11')
    phase_code = table('phase_codes',
                column('sort_order',sa.Integer),
                column('work_type_id',sa.Integer),
                column('ea_act_id',sa.Integer),
                column('start_event',sa.String),
                column('end_event',sa.String),
                column('duration',sa.Integer),
                column('legislated',sa.Boolean),
                column('color',sa.String),
                column('name',sa.String))
    op.bulk_insert(
        phase_code,
        [
            {
                'id': 11,
                'sort_order': 1,
                'name': 'Early Engagement',
                'work_type_id': 6,
                'start_event': 'Initial Project Description accepted',
                'end_event': 'Summary of Engagement Issued',
                'duration': 90,
                'legislated': True,
                'ea_act_id': 3,
                'color': '#E1EBF3'
            },
            {
                'id': 12,
                'sort_order': 2,
                'name': 'Proponent Time: Project Description',
                'work_type_id': 6,
                'start_event': 'Day after the posting of Summary of Engagment',
                'end_event': 'Day before the submission of DPD',
                'duration': 365,
                'legislated': False,
                'ea_act_id': 3,
                'color': '#CCFFFF'
            },
            {
                'id': 13,
                'sort_order': 3,
                'name': 'Readiness Decision',
                'work_type_id': 6,
                'start_event': 'Submission of DPD',
                'end_event': 'Ministers\' Decision',
                'duration': 60,
                'legislated': False,
                'ea_act_id': 3,
                'color': '#C3D7E8'
            }, {
                'id': 14,
            'sort_order': 4,
            'name': 'Process Planning',
            'work_type_id': 6,
            'start_event': 'Day after Ministers\' Decision',
            'end_event': 'Process Order Issued',
            'duration': 120,
            'legislated': True,
            'ea_act_id': 3,
            'color': '#A6C3DD'
        }, {
            'id': 15,
            'sort_order': 5,
            'name': 'Proponent Time: Application Development',
            'work_type_id': 6,
            'start_event': 'Day after Process Order issued',
            'end_event': 'Day before the acceptance of the Application',
            'duration': 1095,
            'legislated': False,
            'ea_act_id': 3,
            'color': '#CCFFFF'
        }, {
            'id': 16,
            'sort_order': 6,
            'name': 'Application Development & Review',
            'work_type_id': 6,
            'start_event': 'Application for an EAC accepted',
            'end_event': 'Notice Regarding Application',
            'duration': 180,
            'legislated': True,
            'ea_act_id': 3,
            'color': '#FAEADC'
        }, {
            'id': 17,
            'sort_order': 7,
            'name': 'Proponent Time: Revised Application',
            'work_type_id': 6,
            'start_event': 'Day after Notice',
            'end_event': 'Day before Revised Application',
            'duration': 365,
            'legislated': False,
            'ea_act_id': 3,
            'color': '#CCFFFF'
        }, {
            'id': 18,
            'sort_order': 8,
            'name': 'Effects Assessment',
            'work_type_id': 6,
            'start_event': 'Revised Application Submitted',
            'end_event': 'Draft Assessment Report is issued',
            'duration': 110,
            'legislated': True,
            'ea_act_id': 3,
            'color': '#F6D5B9'
        }, {
            'id': 19,
            'sort_order': 9,
            'name': 'Recommendation',
            'work_type_id': 6,
            'start_event': 'PECP starts for Draft Assessment Report?',
            'end_event': 'Package sent to Ministers',
            'duration': 40,
            'legislated': True,
            'ea_act_id': 3,
            'color': '#F2C096'
        }, {
            'id': 20,
            'sort_order': 10,
            'name': 'Referral/Decision',
            'work_type_id': 6,
            'start_event': 'Referral Package Received',
            'end_event': 'Minister\'s Decision',
            'duration': 30,
            'legislated': True,
            'ea_act_id': 3,
            'color': '#F2C096'
        }
        ])
    # # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('projects', 'abbreviation')

    op.add_column('milestones', sa.Column('is_start_event', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('milestones', sa.Column('is_end_event', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('milestones', 'auto')
    op.drop_column('milestones', 'kind')
    op.drop_column('milestones', 'duration')
    op.drop_column('milestones', 'start_at')
    milestone = table('milestones', 
                        column('name',sa.String),
                        column('phase_id',sa.Integer),
                        column('milestone_type_id',sa.Integer),
                        column('sort_order',sa.Integer),
                        column('is_start_event',sa.Boolean),
                        column('is_end_event',sa.Boolean))
    op.bulk_insert(milestone,
    [
	{
		"name" : "Submission of IPD & Engagement Plan",
		"phase_id" : 11,
		"milestone_type_id" : 16,
		"sort_order" : 1,
		"is_start_event": True,
		"is_end_event": False
	},
	{
		"name" : "PECP",
		"phase_id" : 11,
		"milestone_type_id" : 11,
		"sort_order" : 2,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Open House",
		"phase_id" : 11,
		"milestone_type_id" : 6,
		"sort_order" : 3,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Virtual Open House",
		"phase_id" : 11,
		"milestone_type_id" : 17,
		"sort_order" : 4,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Summary of Engagement",
		"phase_id" : 11,
		"milestone_type_id" : 13,
		"sort_order" : 5,
		"is_start_event": False,
		"is_end_event": True
	},
	{
		"name" : "Project Withdrawn",
		"phase_id" : 11,
		"milestone_type_id" : 1,
		"sort_order" : 6,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Other",
		"phase_id" : 11,
		"milestone_type_id" : 8,
		"sort_order" : 7,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "EE: Proponent Time",
		"phase_id" : 12,
		"milestone_type_id" : 12,
		"sort_order" : 8,
		"is_start_event": True,
		"is_end_event": True
	},
	{
		"name" : "Project Termination (s.39)",
		"phase_id" : 12,
		"milestone_type_id" : 1,
		"sort_order" : 9,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Other",
		"phase_id" : 12,
		"milestone_type_id" : 8,
		"sort_order" : 10,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Submission of DPD",
		"phase_id" : 13,
		"milestone_type_id" : 16,
		"sort_order" : 11,
		"is_start_event": True,
		"is_end_event": False
	},
	{
		"name" : "Report & Referral",
		"phase_id" : 13,
		"milestone_type_id" : 13,
		"sort_order" : 12,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Readiness Decision",
		"phase_id" : 13,
		"milestone_type_id" : 4,
		"sort_order" : 13,
		"is_start_event": False,
		"is_end_event": True
	},
	{
		"name" : "Other",
		"phase_id" : 13,
		"milestone_type_id" : 8,
		"sort_order" : 14,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Draft Process Order Submission",
		"phase_id" : 14,
		"milestone_type_id" : 16,
		"sort_order" : 15,
		"is_start_event": True,
		"is_end_event": False
	},
	{
		"name" : "PECP",
		"phase_id" : 14,
		"milestone_type_id" : 11,
		"sort_order" : 16,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Open House",
		"phase_id" : 14,
		"milestone_type_id" : 6,
		"sort_order" : 17,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Virtual Open House",
		"phase_id" : 14,
		"milestone_type_id" : 17,
		"sort_order" : 18,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Process Order Issued",
		"phase_id" : 14,
		"milestone_type_id" : 7,
		"sort_order" : 19,
		"is_start_event": False,
		"is_end_event": True
	},
	{
		"name" : "Project Withdrawn",
		"phase_id" : 14,
		"milestone_type_id" : 1,
		"sort_order" : 20,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Other",
		"phase_id" : 14,
		"milestone_type_id" : 8,
		"sort_order" : 21,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "ADR: Proponent Time",
		"phase_id" : 15,
		"milestone_type_id" : 12,
		"sort_order" : 22,
		"is_start_event": True,
		"is_end_event": True
	},
	{
		"name" : "Project Termination (s.39)",
		"phase_id" : 15,
		"milestone_type_id" : 1,
		"sort_order" : 23,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Process Order Amended (s.19)",
		"phase_id" : 15,
		"milestone_type_id" : 7,
		"sort_order" : 24,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Other",
		"phase_id" : 15,
		"milestone_type_id" : 8,
		"sort_order" : 25,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Draft Application Submission",
		"phase_id" : 16,
		"milestone_type_id" : 16,
		"sort_order" : 26,
		"is_start_event": True,
		"is_end_event": False
	},
	{
		"name" : "PECP",
		"phase_id" : 16,
		"milestone_type_id" : 11,
		"sort_order" : 27,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Open House",
		"phase_id" : 16,
		"milestone_type_id" : 6,
		"sort_order" : 28,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Virtual Open House",
		"phase_id" : 16,
		"milestone_type_id" : 17,
		"sort_order" : 29,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Process Order Amended (s.19)",
		"phase_id" : 16,
		"milestone_type_id" : 7,
		"sort_order" : 30,
		"is_start_event": False,
		"is_end_event": True
	},
	{
		"name" : "Project Withdrawn",
		"phase_id" : 16,
		"milestone_type_id" : 1,
		"sort_order" : 31,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Other",
		"phase_id" : 16,
		"milestone_type_id" : 8,
		"sort_order" : 32,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "ADR: Proponent Time",
		"phase_id" : 17,
		"milestone_type_id" : 12,
		"sort_order" : 33,
		"is_start_event": True,
		"is_end_event": True
	},
	{
		"name" : "Project Termination (s.39)",
		"phase_id" : 17,
		"milestone_type_id" : 1,
		"sort_order" : 34,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Process Order Amended (s.19)",
		"phase_id" : 17,
		"milestone_type_id" : 7,
		"sort_order" : 35,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Other",
		"phase_id" : 17,
		"milestone_type_id" : 8,
		"sort_order" : 36,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Application Submission",
		"phase_id" : 18,
		"milestone_type_id" : 16,
		"sort_order" : 37,
		"is_start_event": True,
		"is_end_event": False
	},
	{
		"name" : "Process Order Amended (s.19)",
		"phase_id" : 18,
		"milestone_type_id" : 7,
		"sort_order" : 38,
		"is_start_event": False,
		"is_end_event": True
	},
	{
		"name" : "Project Withdrawn",
		"phase_id" : 18,
		"milestone_type_id" : 1,
		"sort_order" : 39,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Other",
		"phase_id" : 18,
		"milestone_type_id" : 8,
		"sort_order" : 40,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Draft Assessment Report",
		"phase_id" : 19,
		"milestone_type_id" : 13,
		"sort_order" : 41,
		"is_start_event": True,
		"is_end_event": False
	},
	{
		"name" : "PECP",
		"phase_id" : 19,
		"milestone_type_id" : 11,
		"sort_order" : 42,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Open House",
		"phase_id" : 19,
		"milestone_type_id" : 6,
		"sort_order" : 43,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Virtual Open House",
		"phase_id" : 19,
		"milestone_type_id" : 17,
		"sort_order" : 44,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Process Order Amended (s.19)",
		"phase_id" : 19,
		"milestone_type_id" : 7,
		"sort_order" : 45,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Project Withdrawn",
		"phase_id" : 19,
		"milestone_type_id" : 1,
		"sort_order" : 46,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Other",
		"phase_id" : 19,
		"milestone_type_id" : 8,
		"sort_order" : 47,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "Referral Package Received",
		"phase_id" : 20,
		"milestone_type_id" : 16,
		"sort_order" : 48,
		"is_start_event": True,
		"is_end_event": False
	},
	{
		"name" : "Minister Meeting",
		"phase_id" : 20,
		"milestone_type_id" : 3,
		"sort_order" : 49,
		"is_start_event": False,
		"is_end_event": False
	},
	{
		"name" : "EAC Decision",
		"phase_id" : 20,
		"milestone_type_id" : 4,
		"sort_order" : 50,
		"is_start_event": False,
		"is_end_event": True
	},
	{
		"name" : "Other",
		"phase_id" : 20,
		"milestone_type_id" : 8,
		"sort_order" : 51,
		"is_start_event": False,
		"is_end_event": False
	}
])
    # ### end Alembic commands ###
