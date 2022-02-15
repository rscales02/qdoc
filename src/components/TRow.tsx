import { FC } from "react";

interface ITRowProps {
  name: string
  value: string
};

export const TRow : FC<ITRowProps> = (props) => {
    let name = props.name
    let value = props.value

    return (
        <tr className='card'>
            <td>{name}</td>
            <td>{value}</td>
        </tr>
    );
}
