login = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "login": {
      "type": "string"
    },
    "fam_inner": {
      "type": "string"
    },
    "phone_inner": {
      "type": "string"
    },
    "phone_inner2": {
      "type": "null"
    },
    "email_inner": {
      "type": "string"
    },
    "bonuses": {
      "type": "null"
    },
    "activ": {
      "type": "integer"
    },
    "confirm_email": {
      "type": "integer"
    },
    "confirm_phone": {
      "type": "integer"
    },
    "normalphone": {
      "type": "string"
    },
    "normalphone2": {
      "type": "null"
    },
    "nickname": {
      "type": "string"
    },
    "avatar_id": {
      "type": "integer"
    },
    "background_id": {
      "type": "null"
    },
    "needs_manager_confirmation": {
      "type": "integer"
    },
    "verified": {
      "type": "integer"
    },
    "avatar_achievement": {
      "type": "null"
    },
    "custom_avatar": {
      "type": "null"
    },
    "is_review_notification_enabled": {
      "type": "boolean"
    },
    "notification_settings": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "key": {
              "type": "string"
            },
            "active": {
              "type": "boolean"
            },
            "title": {
              "type": "string"
            }
          },
          "required": [
            "key",
            "active",
            "title"
          ]
        },
        {
          "type": "object",
          "properties": {
            "key": {
              "type": "string"
            },
            "active": {
              "type": "boolean"
            },
            "title": {
              "type": "string"
            }
          },
          "required": [
            "key",
            "active",
            "title"
          ]
        },
        {
          "type": "object",
          "properties": {
            "key": {
              "type": "string"
            },
            "active": {
              "type": "boolean"
            },
            "title": {
              "type": "string"
            }
          },
          "required": [
            "key",
            "active",
            "title"
          ]
        },
        {
          "type": "object",
          "properties": {
            "key": {
              "type": "string"
            },
            "active": {
              "type": "boolean"
            },
            "title": {
              "type": "string"
            }
          },
          "required": [
            "key",
            "active",
            "title"
          ]
        },
        {
          "type": "object",
          "properties": {
            "key": {
              "type": "string"
            },
            "active": {
              "type": "boolean"
            },
            "title": {
              "type": "string"
            }
          },
          "required": [
            "key",
            "active",
            "title"
          ]
        }
      ]
    },
    "compare_goods": {
      "type": "array",
      "items": {}
    },
    "wishlists_goods": {
      "type": "array",
      "items": [
        {
          "type": "integer"
        }
      ]
    },
    "business": {
      "type": "object",
      "properties": {
        "level": {
          "type": "object",
          "properties": {
            "id": {
              "type": "integer"
            },
            "title": {
              "type": "string"
            },
            "description": {
              "type": "string"
            },
            "ord": {
              "type": "integer"
            },
            "required_balance": {
              "type": "integer"
            },
            "bonus_percentage": {
              "type": "number"
            },
            "clients_count": {
              "type": "integer"
            },
            "offers_count": {
              "type": "integer"
            },
            "offers_total": {
              "type": "integer"
            },
            "offers_average": {
              "type": "integer"
            },
            "bonuses": {
              "type": "integer"
            },
            "photo": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "integer"
                    },
                    "src": {
                      "type": "string"
                    },
                    "full_src": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "name",
                    "src",
                    "full_src"
                  ]
                }
              ]
            },
            "bonus_percentage_percent": {
              "type": "number"
            }
          },
          "required": [
            "id",
            "title",
            "description",
            "ord",
            "required_balance",
            "bonus_percentage",
            "clients_count",
            "offers_count",
            "offers_total",
            "offers_average",
            "bonuses",
            "photo",
            "bonus_percentage_percent"
          ]
        },
        "nextLevel": {
          "type": "object",
          "properties": {
            "id": {
              "type": "integer"
            },
            "title": {
              "type": "string"
            },
            "description": {
              "type": "string"
            },
            "ord": {
              "type": "integer"
            },
            "required_balance": {
              "type": "integer"
            },
            "bonus_percentage": {
              "type": "number"
            },
            "clients_count": {
              "type": "integer"
            },
            "offers_count": {
              "type": "integer"
            },
            "offers_total": {
              "type": "integer"
            },
            "offers_average": {
              "type": "integer"
            },
            "bonuses": {
              "type": "integer"
            },
            "photo": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "integer"
                    },
                    "src": {
                      "type": "string"
                    },
                    "full_src": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "name",
                    "src",
                    "full_src"
                  ]
                }
              ]
            },
            "bonus_percentage_percent": {
              "type": "number"
            }
          },
          "required": [
            "id",
            "title",
            "description",
            "ord",
            "required_balance",
            "bonus_percentage",
            "clients_count",
            "offers_count",
            "offers_total",
            "offers_average",
            "bonuses",
            "photo",
            "bonus_percentage_percent"
          ]
        },
        "nextMoney": {
          "type": "integer"
        },
        "progress": {
          "type": "integer"
        }
      },
      "required": [
        "level",
        "nextLevel",
        "nextMoney",
        "progress"
      ]
    },
    "basket": {
      "type": "null"
    }
  },
  "required": [
    "id",
    "login",
    "fam_inner",
    "phone_inner",
    "phone_inner2",
    "email_inner",
    "bonuses",
    "activ",
    "confirm_email",
    "confirm_phone",
    "normalphone",
    "normalphone2",
    "nickname",
    "avatar_id",
    "background_id",
    "needs_manager_confirmation",
    "verified",
    "avatar_achievement",
    "custom_avatar",
    "is_review_notification_enabled",
    "notification_settings",
    "compare_goods",
    "wishlists_goods",
    "business",
    "basket"
  ]
}