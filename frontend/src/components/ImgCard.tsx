import { FC } from "react";
import {Card, CardMedia, CardContent, Typography} from '@mui/material/'

interface IImgCardProps {
  src: string
  title: string
  text: string
};

export const ImgCard: FC<IImgCardProps> = (props) => {
    return (
      <Card>
        <CardMedia
          component="img"
          height="194"
          image={props.src}
          alt={props.text}></CardMedia>
        <CardContent>
        <Typography gutterBottom variant="h5" component="div">
          {props.title}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          {props.text}
        </Typography>
      </CardContent>
      </Card>
    );
}
