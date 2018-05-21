import json

from collections import defaultdict

in_dir = 'data'
out_dir = 'json'


def run():
    movie_id2tags = map_movie_id_to_tags()
    movie_id2ratings = map_movie_id_to_ratings()
    write_movies_json(movie_id2tags, movie_id2ratings)


def write_movies_json(movie_id2tags, movie_id2ratings):
    """
    MovieID::Title::Genres
    1::Toy Story (1995)::Adventure|Animation|Children|Comedy|Fantasy
    """
    name = 'movies'
    with open(f'{in_dir}/{name}.dat') as file, \
            open(f'{out_dir}/{name}-sum.json', mode='w') as w:
        w.write('[')
        comma = ''
        for raw in file:
            line = raw.strip('\n').split('::')
            movie_id = int(line[0])
            genres = line[2].split('|')
            ratings = movie_id2ratings[movie_id]
            """
            ╔═══════════════╗
            ║ MovieID       ║
            ╠═══════════════╣
            ║ Title         ║
            ╠═══════════════╣
            ║ Genres        ║
            ╠══════╦════════╣
            ║ Tags ║ UserID ║
            ║      ╠════════╣
            ║      ║ Tag    ║
            ╠══════╩════════╣
            ║ RatingMax     ║
            ╠═══════════════╣
            ║ RatingMin     ║
            ╠═══════════════╣
            ║ RatingCnt     ║
            ╠═══════════════╣
            ║ RatingAve     ║
            ╚═══════════════╝
            """
            row = {'MovieID': movie_id,
                   'Title': line[1],
                   'Tags': movie_id2tags[movie_id],
                   #'Ratings': ratings,
                   'RatingMax': max(ratings) if ratings else None,
                   'RatingMin': min(ratings) if ratings else None,
                   'RatingCnt': len(ratings) if ratings else None,
                   'RatingAve': sum(ratings) / len(ratings) if ratings else None,
                   'Genres': genres
                   }
        #print(row)
            out = json.dumps(row)
            w.write(comma + out + '\n')
            comma = ','
        w.write('\n]')


def map_movie_id_to_tags():
    """
    15::4973::excellent!::1215184630
    20::1747::politics::1188263867
    """
    name = 'tags'
    id2tags = defaultdict(list)
    with open(f'{in_dir}/{name}.dat') as file:
        for raw in file:
            line = raw.strip('\n').split('::')
            movie_id = int(line[1])
            tag = {'UserID': int(line[0]),
                   #'MovieID': movie_id,
                   'Tag': line[2],
                   #'Timestamp': int(line[3])
                   }
            id2tags[movie_id] += [tag]
    return id2tags


def map_movie_id_to_ratings():
    """
    UserID::MovieID::Rating::Timestamp
    1::122::5::838985046
    """
    name = 'ratings'
    id2ratings = defaultdict(list)
    with open(f'{in_dir}/{name}.dat') as file:
        for raw in file:
            line = raw.strip('\n').split('::')
            movie_id = int(line[1])
            rating = float(line[2])
            id2ratings[movie_id] += [rating]
    return id2ratings

if __name__ == '__main__':
    run()