# User
| Name      | PK | AI | FK | Null | Type         |
|-----------|----|----|----|------|--------------|
| id        | 1  | 1  | 0  | 0    | int          |
| stdId     | 0  | 0  | 0  | 0    | varchar(6)   |
| name      | 0  | 0  | 0  | 0    | varchar(8)   |
| password  | 0  | 0  | 0  | 0    | varchar(500) |
| authority | 0  | 0  | 0  | 0    | int          |

# PlaylistInfo
| Name        | PK | AI | FK | Null | Type         |
|-------------|----|----|----|------|--------------|
| id          | 1  | 1  | 0  | 0    | int          |
| owner       | 0  | 0  | 1  | 0    | varchar(6)   |
| title       | 0  | 0  | 0  | 0    | varchar(100) |
| description | 0  | 0  | 0  | 0    | varchar(500) |
| create_time | 0  | 0  | 0  | 0    | datetime     |

# Playlist
| Name   | PK | AI | FK | Null | Type |
|--------|----|----|----|------|------|
| id     | 1  | 1  | 0  | 0    | int  |
| infoId | 0  | 0  | 1  | 0    | int  |
| songId | 0  | 0  | 1  | 0    | int  |

# Song
| Name          | PK | AI | FK | Null | Type         |
|---------------|----|----|----|------|--------------|
| id            | 1  | 1  | 0  | 0    | int          |
| title         | 0  | 0  | 0  | 0    | varchar(100) |
| length        | 0  | 0  | 0  | 0    | int          |
| url           | 0  | 0  | 0  | 0    | varchar(500) |
| thumbnail_url | 0  | 0  | 0  | 1    | varchar(500) |

