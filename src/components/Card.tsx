import { FC } from "react";

interface ICardProps {
  name: string
  currentPrice: string
};

export const Card : FC<ICardProps> = (props) => {
    let name = props.name
    let currentPrice = props.currentPrice

    return (
        <tr className='card'>
            <td>{name}</td>
            <td>{currentPrice}</td>
        </tr>
    );
}
