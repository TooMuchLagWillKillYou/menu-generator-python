# PDF MENU GENERATOR

The goal of this project is to automatically create a menu given the list of items,
language, format, and styling rules such as font family, colors, and so on.

The menu can be exported in different formats containg different items. Not all formats contain all the items.
The menu can be translated in one or multiple languages between the below-mentioned.

Items are grouped into categories. An item's category affects the way the item is placed on the page.

The system should start placing the items in the same order that they are found,
without changing the order for ny reason.
The system should understand when the current page is full and it's time to create another one.

All this work was done manually evertime a price, or an item was added or edited. That's way this project was born.

## Constraints and guidelines

```
Categories: [
    { 'id':1,   'name': 'Specialty'     },
    { 'id':2,   'name': 'Classic'       },
    { 'id':3,   'name': 'Aperitif'      },
    { 'id':4,   'name': 'Drink'         },
    { 'id':5,   'name': 'Draft beers'   },
    { 'id':6,   'name': 'Bottle beers'  },
    { 'id':7,   'name': 'Wine'          },
    { 'id':8,   'name': 'Cakes'         },
    { 'id':9,   'name': 'Cocktails'     },
    { 'id':10,  'name': 'Digestif'      },
    { 'id':11,  'name': 'Grappa'        },
    { 'id':12,  'name': 'Coffee'        }
]

Languages: [ 'Italian (default)', 'English', 'German' ]

Formats: [
    {
        'name':         'table',
        'size':         '148x210mm',
        'categories':   [ 1, 2, 3, 4, 5, 6, 7 ],
        'description':  'Most important format, it is given to the restaurant's guests at the beginning of the serving'
    },
    {
        'name':         'dessert',
        'size':         '148x210mm',
        'categories':   [ 8, 9, 10, 11, 12 ],
        'description':  'It is given to the restaurant's customers after they had eaten the main serving'
    },
    {
        'name':         'instagram',
        'size':         '1080x1350px',
        'categories':   [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ],
        'description':  'Contains everything, it is uploaded on the restaurant's Instagram profile'
    }
]

Colors: [
    { 'name': '', 'code': '' },
    { 'name': '', 'code': '' },
    { 'name': '', 'code': '' }
]
```

## Flow:

0. User chooses language and format to generate the menu
1. Read the list of menu items from a .csv file or from a database
2. Pic the items translation based on user's selected language
3. Load the menu template
4. Start placing the items inside the menu
5. LLM will decide if it's time to create a new page
6. Export into required format

## Files, directories

- main.py: entry point
- src/schemas.py: classes
- menu-items.csv: data source
- example.pdf: output example
- requirements.txt: dependencies
